'''
    Nome: criacaoTabela
    Autor: Thiago
    Função: criação da tabela
'''

from conexao import cur # iomporta a função cur do arquivo conexao
import psycopg2 # drive
from psycopg2 import OperationalError

try:
    cur.execute("CREATE TABLE alimentos(id INT PRIMARY KEY, nome VARCHAR, valor FLOAT)") # executa uma CRUD
    print("Tabela criada") #exibe mensgem caso tabela seja craida

except OperationalError as e:
        print(f"Erro ao criar tabela no PostgreSQL: {e}") # exibi mensagem contendo a mensagem de erro