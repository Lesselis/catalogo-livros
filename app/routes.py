from crypt import methods

from flask import render_template, request, redirect, url_for
from app import app
from app.services import carregar_livros, adicionar_livro, editar_livro, deletar_livro
from app.models import Livro

@app.route('/')
def index():
    livros = carregar_livros()
    return render_template('index.html', livros=livros)

@app.route('/add', methods=['GET', 'POST'])
def adicionar_livro_rota():
    if request.method == 'POST':
        novo_livro = Livro(
            id=None,
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            genero=request.form['genero'],
            ano=request.form['ano']
        )
        adicionar_livro(novo_livro)
        return redirect(url_for('index'))
    return render_template('add_livro.html')

@app.route('/edit/<int:id_livro>', methods=['GET', 'POST'])
def editar_livro_rota(id_livro):
    livros = carregar_livros()
    livro = next((livro for livro in livros if livro.id == id_livro), None)
    if request.method == 'POST':
        livro_atualizado = Livro(
            id=id_livro,
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            genero=request.form['genero'],
            ano=request.form['ano']
        )
        editar_livro(id_livro, livro_atualizado)
        return redirect(url_for('index'))
    return render_template('edit_livro.html', livro=livro, id_livro=id_livro)

@app.route('/delete/<int:id_livro>', methods=['POST'])
def deletar_livro_rota(id_livro):
    deletar_livro(id_livro)
    return redirect(url_for('index'))

@app.route('/delete/confirm/<int:id_livro>', methods=['GET'])
def confirmar_deletar_livro_rota(id_livro):
    livros = carregar_livros()
    livro = next((livro for livro in livros if livro.id == id_livro), None)
    return render_template('delete_livro.html', livro=livro, id_livro=id_livro)