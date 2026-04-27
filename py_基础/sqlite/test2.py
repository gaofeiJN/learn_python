import sqlite3


def main():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    cur.execute(
        """
SELECT * FROM users
"""
    )
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main()
