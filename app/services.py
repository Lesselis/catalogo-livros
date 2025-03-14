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
    novo_id = max ([livro.id for livro in livros], default=0) + 1
    novo_livro.id = novo_id
    livros.append(novo_livro)
    salvar_livros(livros)

def editar_livro(id_livro, livro_atualizado):
    livros = carregar_livros()
    for index, livro in enumerate(livros):
        if livro.id == id_livro:
            livros[index] = livro_atualizado
            break
    salvar_livros(livros)

def deletar_livro(id_livro):
    livros = carregar_livros()
    livros = [livro for livro in livros if livro.id != id_livro]
    salvar_livros(livros)