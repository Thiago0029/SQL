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
        user =  "postgres",
        password = '123',
        host = '192.168.1.13',
        port = '5432'
    )

    cur = conexao.cursor()
    print ("Conexão ok")
    cur.execute ("CREATE TABLE alimentos(id INT PRIMARY KEY, nome VARCHAR(100), valor FLOAT)")

except OperationalError as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

finally:
    if conexao:
        conexao.close()