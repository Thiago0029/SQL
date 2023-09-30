'''
    Nome: craicaoTabela
    Author: Thiago
    Função: Seleciona tabela 
'''

import psycopg2
from psycopg2 import OperationalError
from conexao import cur

try:
   #Valor da variável que deseja inserir
    valor = "Algum valor"

    # Consulta SQL com um parâmetro
    consulta = "INSERT INTO tabela (coluna) VALUES (%s)"

    # Executar a consulta com o valor da variável
    cur.execute(consulta, (valor,))

    # Confirmar a operação
    cur.commit()

except OperationalError as e:
    print(f"Erro: {e}")