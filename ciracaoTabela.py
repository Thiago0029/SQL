'''
    Nome: criacaoTabela
    Autor: Thiago
    Função: criação da tabela
'''

from conexao import cur # iomporta a função cur do arquivo conexao
import psycopg2 # drive

cur.execute("CREATE TABLE alimentos(id INT PRIMARY KEY, nome VARCHAR, valor FLOAT)") # executa uma CRUD
print("Tabela criada") #exibe mensgem caso tabela seja craida