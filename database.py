import sqlite3
from hashlib import sha256

# Função para criar uma conexão com o banco de dados SQLite
def connect_db():
    conn = sqlite3.connect("users.db")
    return conn

# Função para criar a tabela de usuários (se não existir)
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def verifica_existencia_user(user):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users where username = ?', (user,))
    result = cursor.fetchone()
    conn.close()
    return result

def cadastra_user_no_banco(user, senha):
    hashed_senha = sha256(senha.encode()).hexdigest()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (user, hashed_senha))
    conn.commit()
    conn.close()

def verifica_user_senha(user, senha):
    hashed_senha = sha256(senha.encode()).hexdigest()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users where username = ? and password = ?', (user, hashed_senha,))
    result = cursor.fetchone()
    conn.close()
    return result
