import psycopg2
from flask import *
import dao
from dao import conectardb

app = Flask(__name__)


@app.route('/')
def paginaprincipal():
    return render_template('pag_login_cadastro.html')

@app.route('/exibirpaginacadastro')
def exibir_pagina_cadastro():
    return render_template('cadastro_de_produtos.html')

def inserir_novo_usuario(matricula, nome, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False

    try:
        sql = f"INSERT INTO usuario (login, senha) VALUES ('{matricula}', '{nome}', {senha})"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

#aaaaaaa






app.run(debug=True)