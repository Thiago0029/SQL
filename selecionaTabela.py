'''
    Nome: craicaoTabela
    Author: Thiago
    Função: Seleciona tabela 
'''

import psycopg2
from psycopg2 import OperationalError
from conexao import cur

try:
    cur.execute("SELEC INTO tabela (coluna) values (%s)")
except OperationalError as e:
    print(f"Erro: {e}")