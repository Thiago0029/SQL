'''
    Nome: criacaoTabela
    Autor: Thiago
    Função: criação da tabela
'''

# iomporta a função cur do arquivo conexao
from conexao import cur 

# drive
import psycopg2 
from psycopg2 import OperationalError

try:
    # executa uma CRUD
    cur.execute("CREATE TABLE alimentos(id INT PRIMARY KEY, nome VARCHAR, valor FLOAT)") 
    print("Tabela criada")
    
    #confirma a operação
    cur.commit()

 
except OperationalError as e:
        # exibi mensagem contendo a mensagem de erro
        print(f"Erro ao criar tabela no PostgreSQL: {e}")