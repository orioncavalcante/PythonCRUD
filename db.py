import mysql.connector

# Função para criar e retornar a conexão
def criar_conexao():
    conexao = mysql.connector.connect(
        host='local do banco',
        user='usuario',
        password='senha',
        database='nome do banco'
    )
    return conexao


def criar_cursor(conexao):
    return conexao.cursor()


conexao = criar_conexao()
cursor = criar_cursor(conexao)

cursor.close()
conexao.close()
