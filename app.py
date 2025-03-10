from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import uuid

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Caminho do arquivo JSON
BOOKS_FILE = 'books.json'

# Função para carregar os livros
def carregar_livros():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Função para salvar os livros
def salvar_livros(livros):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    query = request.args.get('query', '').strip().lower()
    livros = carregar_livros()
    if query:
        livros = [l for l in livros if query in l['titulo'].lower() or query in l['autor'].lower()]
    return render_template('index.html', livros=livros, query=query)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        ano = request.form['ano']
        quantidade = int(request.form['quantidade'])

        livros = carregar_livros()
        livros.append({
            'id': str(uuid.uuid4()),  # Gera um ID único para cada livro
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'ano': ano,
            'quantidade': quantidade
        })
        salvar_livros(livros)
        flash('Livro adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_book.html')

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar_livro(id):
    livros = carregar_livros()
    livro = next((l for l in livros if l['id'] == id), None)

    if not livro:
        flash('Livro não encontrado!', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        livro['titulo'] = request.form['titulo']
        livro['autor'] = request.form['autor']
        livro['genero'] = request.form['genero']
        livro['ano'] = request.form['ano']
        livro['quantidade'] = int(request.form['quantidade'])
        salvar_livros(livros)
        flash('Livro atualizado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_book.html', livro=livro)

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_livro(id):
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        livros = json.load(file)

    livros = [livro for livro in livros if livro["id"] != id]

    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(livros, file, indent=4, ensure_ascii=False)

    flash('Livro excluído com sucesso!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
