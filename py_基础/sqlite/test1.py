#!/usr/bin/env python3

import sqlite3

conn = None
c = None


def connect_db():
    global conn
    global c
    conn = sqlite3.connect("test.db")
    c = conn.cursor()


def close_db():
    global conn
    global c

    if c:
        c.close()

    if conn:
        conn.close()


def create_table():
    global conn
    global c

    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL)"""
    )
    conn.commit()


def insert_user(name, age):
    global conn
    global c

    # 判断用户是否已经存在
    c.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    if result:
        print(f"User {name} already exists.")
        return

    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


def query_users():
    global conn
    global c

    c.execute("SELECT * FROM users")
    users = c.fetchall()
    return users


if __name__ == "__main__":
    connect_db()
    create_table()

    insert_user("Alice", 30)
    insert_user("Bob", 25)
    insert_user("gao fei", 39)
    insert_user("wang jin fei", 38)
    insert_user("tao tao", 2)
    insert_user("duo duo", 6)

    users = query_users()
    for user in users:
        print(user)

    close_db()
