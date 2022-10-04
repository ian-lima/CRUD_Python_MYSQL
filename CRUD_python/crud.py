import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdcrud',
)

cursor = conexao.cursor()

# CRUD
nome_produto = "toddynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()

# CREATE
# nome_produto = "chocolate"
# valor = 15 #só número inteiro, pois na tabela foi classificado como número inteiro
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' #não precisa colocar o nome idVendas no insert, pq foi marcado na opção como auto increment, ou seja, ele preenche sozinho
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# UPDATE
# nome_produto = "toddynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"' # aspas duplas no nome do produto, pois é um texto e precisa delas no SQL
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "toddynho"
# comando = f'DELETE vendas WHERE nome_produto = "{nome_produto}"' # aspas duplas no nome do produto, pois é um texto e precisa delas no SQL
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
