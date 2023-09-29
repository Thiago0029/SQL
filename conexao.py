'''
    Nome: conexao.py
    Autor: Thiago
    Função: Realizar a conexão com o banco de dados PostgreSQL
'''
import psycopg2

conexao = psycopg2.connect(
    dbname = "estudos",
    user =  "postgresql",
    passwords = "123",
    host = "192.168.1.13"
)

cur = conexao.cursor()