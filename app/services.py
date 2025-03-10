import json
from app.models import Livro

def carregar_livros():
    with open('data/livros.json', 'r') as file:
        livros_dict = json.load(file)
        return [Livro.de_dict(livro) for livro in livros_dict]

def salvar_livros(livros):
    with open('data/livros.json', 'w') as file:
        json.dump([livro.para_dict() for livro in livros], file, indent=4)

def adicionar_livro(novo_livro):
    livros = carregar_livros()
    livros.append(novo_livro)
    salvar_livros(livros)

def editar_livro(id_livro, livro_atualizado):
    livros = carregar_livros()
    livros[id_livro] = livro_atualizado
    salvar_livros(livros)

def deletar_livro(id_livro):
    livros = carregar_livros()
    livros.pop(id_livro)
    salvar_livros(livros)