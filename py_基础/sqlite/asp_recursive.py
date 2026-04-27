import sqlite3
import csv

sql_stmt = """
WITH RECURSIVE asp_tree(job,jyoken,level) AS (
    SELECT job,jyoken,0 FROM asp WHERE job = ?
    
    UNION ALL

    SELECT o.job,o.jyoken,r.level + 1
    FROM asp as o, asp_tree as r
    WHERE o.job = r.jyoken AND r.level < ?    
    )
SELECT DISTINCT job, jyoken FROM asp_tree
"""


class AspRecursive:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def query(self, job, max_level=5):
        self.cursor.execute(sql_stmt, (job, max_level))

        writer = csv.writer(
            open("asp_recursive_output.csv", "w", encoding="utf-8", newline="")
        )
        for row in self.cursor:
            writer.writerow(row)


def main():
    with AspRecursive("asp.db") as asp:
        asp.query("JOB001", max_level=5)


if __name__ == "__main__":
    main()
