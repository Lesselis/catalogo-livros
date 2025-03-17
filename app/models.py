# Definição do modelo para os dados do livro

class Livro:
    def __init__(self, id, titulo, autor, genero, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

    def converter_para_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "ano": self.ano
        }

    @staticmethod
    def construir_de_dicionario(data):
        return Livro(
            id=data.get("id"),
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            genero=data.get("genero"),
            ano=data.get("ano")
        )