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
    livro = livros[id_livro]
    if request.method == 'POST':
        livro_atualizado = Livro(
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            genero=request.form['genero'],
            ano=request.form['ano']
        )
        editar_livro(id_livro, livro_atualizado)
        return redirect(url_for('index'))
    return render_template('edit_livro.html', livro=livro, id_livro=id_livro)

@app.route('/delete/<int:id_livro>')
def deletar_livro_rota(id_livro):
    deletar_livro(id_livro)
    return redirect(url_for('index'))