'''
    Nome: conexao.py
    Autor: Thiago
    Função: Realizar a conexão com o banco de dados PostgreSQL
'''
import psycopg2 # importa o drive psycopg2 para conexão com o POStgreSQL
from psycopg2 import OperationalError # importa função para tratamento de erro 

try: # funcionamento normal do códio
    conexao = psycopg2.connect( # salva os dados para conexão com Postgresql
        dbname = "estudos", #
        user =  "postgres", #
        password = '123', # dados da conexão
        host = '192.168.1.7', #
        port = '5432' #
    )

    cur = conexao.cursor() # inicia a conexão
    print ("Conexão ok") # exibi confirmação da conexão

except OperationalError as e: # chamda caso ocorra erro para efetuar conexão
    print(f"Erro ao conectar ao PostgreSQL: {e}") # exibi mensagem contendo a mensagem de erro