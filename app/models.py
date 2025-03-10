# Definição do modelo para os dados do livro

class Livro:
    def __init__(self, titulo, autor, genero, ano):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

    def para_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "ano": self.ano
        }

    @staticmethod
    def de_dict(data):
        return Livro(
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            genero=data.get("genero"),
            ano=data.get("ano")
        )