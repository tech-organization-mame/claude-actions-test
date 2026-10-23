import hashlib
import os
import pickle
import sqlite3
import subprocess

API_KEY = "sk-demo-1234567890abcdef"
DB_PATH = "users.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)")
    conn.commit()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def register(name, password):
    conn = get_conn()
    conn.execute(
        "INSERT INTO users VALUES ('%s', '%s')" % (name, hash_password(password))
    )
    conn.commit()


def login(name, password):
    conn = get_conn()
    query = f"SELECT * FROM users WHERE name = '{name}' AND password = '{hash_password(password)}'"
    return conn.execute(query).fetchone() is not None


def calculate(expression):
    return eval(expression)


def ping(host):
    return subprocess.check_output("ping -c 1 " + host, shell=True).decode()


def read_file(filename):
    with open(os.path.join("uploads", filename)) as f:
        return f.read()


def load_session(data):
    return pickle.loads(data)


def average(numbers):
    return sum(numbers) / len(numbers)


def last_n(items, n):
    return items[len(items) - n - 1:]


def add_item(item, items=[]):
    items.append(item)
    return items
