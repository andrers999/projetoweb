import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='dpg-cu2lg29opnds73f0v1hg-a.oregon-postgres.render.com',
        database='projetoarmazem',
        user='projetoarmazem_user',
        password='jAo6s5tivjEKU6bQUlkijCCsV57aFsIM'
    )
    return con
#------------------------CADASTRO E LOGIN------------------------
def inserirusuario(matricula, nome, senha):
    #método para
    # conectar o banco de dados, retornando a conexao com jacas
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (matricula, nome, senha) VALUES ('{matricula}', '{nome}', '{senha}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def verificarlogin(matricula, senha, conexao):

    cur = conexao.cursor()
    cur.execute(f"SELECT matricula, nome FROM usuarios WHERE matricula = '{matricula}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset
#------------------------------------------------

#------------------------CADASTRO DE PRODUTOS------------------------
def add_NVproduto(id, nome, preco, quantidade):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO produtos (id, nome, preco, quantidade) VALUES ('{id}', '{nome}', '{preco}', {quantidade})"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito
#------------------------------------------------

# ------------------------REMOVER PRODUTOS------------------------
def remov_produto(nome):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"DELETE FROM produtos WHERE nome = '{nome}'"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

#------------------------------------------------

# ------------------------LISTA DE PRODUTOS------------------------
def buscar_produtos():
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute("SELECT id, nome, preco, quantidade FROM produtos")
    produtos = cur.fetchall()
    conexao.close()
    print(produtos)  # Adicione isto para verificar os dados recuperados
    return produtos
#------------------------------------------------
