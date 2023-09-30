'''
    Nome: conexao.py
    Autor: Thiago
    Função: Realizar a conexão com o banco de dados PostgreSQL
'''

# importa o drive psycopg2 para conexão com o POStgreSQL
import psycopg2 

# importa função para tratamento de erro 
from psycopg2 import OperationalError 

try:
    # salva os dados para conexão com Postgresql
    conexao = psycopg2.connect( 
        dbname = "estudos", #
        user =  "postgres", #
        password = '123', # dados da conexão
        host = '192.168.1.7', #
        port = '5432' #
    )

    # inicia a conexão
    cur = conexao.cursor()
     # exibi confirmação da conexão
    print ("Conexão ok") 

# chamda caso ocorra erro para efetuar conexão
except OperationalError as e: 
    # exibi mensagem contendo a mensagem de erro
    print(f"Erro ao conectar ao PostgreSQL: {e}") 