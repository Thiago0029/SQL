'''
    Nome: criacaoTabela
    Autor: Thiago
    Função: criação da tabela

from conexao import cur
import psycopg2

cur.execute ("CREATE TABLE alimentos(PRIMARY KEY id INT(3), nome VARCHAR(100), valor FLOAT(2.2))")
'''