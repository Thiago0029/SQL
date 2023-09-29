'''
    Nome: criacaoTabela
    Autor: Thiago
    Função: criação da tabela
'''

from conexao import cur
import psycopg2

cur.execute("CREATE TABLE alimentos(id INT PRIMARY KEY, nome VARCHAR, valor FLOAT)")
print("Tabela criada")