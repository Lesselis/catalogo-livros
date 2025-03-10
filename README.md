# Catálogo de Livros

Este é um projeto de catálogo de livros desenvolvido com Flask. Ele permite adicionar, editar e deletar livros, além de exibir uma lista de livros cadastrados.

## Instalação

1. Clone o repositório:
   ```https
   git clone [https://github.com/seu-usuario/catalogo-de-livros.git](https://github.com/Lesselis/catalogo-livros.git)](https://github.com/Lesselis/catalogo-livros.git)
  
   ```

2. Crie e ative um ambiente virtual:
   - No Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Execução

1. Inicie a aplicação Flask:
   ```sh
   flask run
   ```

2. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:5000/
   ```

## Funcionalidades

- **Página Inicial**: Exibe a lista de livros cadastrados.
- **Adicionar Livro**: Permite adicionar um novo livro ao catálogo.
- **Editar Livro**: Permite editar as informações de um livro existente.
- **Deletar Livro**: Permite deletar um livro do catálogo.

## Estrutura dos Arquivos

### `app/__init__.py`
Configura a aplicação Flask.

### `app/routes.py`
Define as rotas da aplicação.

### `app/models.py`
Define o modelo de dados para os livros.

### `app/services.py`
Contém funções para carregar, salvar, adicionar, editar e deletar livros.

### `app/static/styles.css`
Contém os estilos CSS para a aplicação.

### `app/templates/`
Contém os templates HTML para renderização das páginas.

### `data/livros.json`
Armazena os dados dos livros em formato JSON.

## Observações

- Certifique-se de que o ambiente virtual esteja ativado ao instalar as dependências e executar a aplicação.
