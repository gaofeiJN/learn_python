import sqlite3
import csv

conn = None
cursor = None


def create_table():
    global conn
    global cursor

    conn = sqlite3.connect("asp.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS asp (
            job TEXT NOT NULL,
            jyoken TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_asp_job ON asp (job)
        """
    )
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_asp_jyoken ON asp (jyoken)
        """
    )
    conn.commit()


def insert_data(job, jyoken):
    global conn
    global cursor

    cursor.execute(
        """
        INSERT INTO asp (job, jyoken) VALUES (?, ?)
        """,
        (job, jyoken),
    )
    conn.commit()


def close_db():
    global conn
    global cursor

    if cursor:
        cursor.close()

    if conn:
        conn.close()


def main():
    create_table()

    reader = csv.reader(open("asp.csv", "r", encoding="utf-8"))
    for row in reader:
        insert_data(row[0], row[1])

    close_db()


if __name__ == "__main__":
    main()
