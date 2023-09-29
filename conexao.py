'''
    Nome: conexao.py
    Autor: Thiago
    Função: Realizar a conexão com o banco de dados PostgreSQL
'''
import psycopg2
from psycopg2 import OperationalError
try:
    conexao = psycopg2.connect(
        dbname = "estudos",
        user =  "postgresql",
        password = "123",
        host = "192.168.1.13"
    )

    cur = conexao.cursor()

except OperationalError as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")