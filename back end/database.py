import psycopg2
from psycopg2 import sql, errors

def create_database():
    conexao = psycopg2.connect( 
        host = 'localhost',
        database = 'postres',
        user = 'postgres'
        password = 'otavioberti'
    )
    conexao.autocommit = True
    cursor = conexao.cursor()

    try:
        cursor.execute('CREATE DATABASE Nublack')
        print("Banco de dados criado com sucesso")

    except errors.DuplicateDatabase:
        print("O banco de dados Nublack ja esta criado")

    except Exception as e :
        print(f"Erro ao criar o banco de dados {e}")

    finally:
        conexao.close()
        cursor.close()

def connect_database():
    try:
        conexao = psycopg2.connect(
        host = 'localhost',
        database = 'Nublack',
        user = 'postgres'
        password = 'otavioberti'
        )
        print("Conectado ao banco de dados com sucesso")
        return conexao
    
    except Exception as e :
        print("Erro ao conectar com o banco de dados: {e}")
        return None