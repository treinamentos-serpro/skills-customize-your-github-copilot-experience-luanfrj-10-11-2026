# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com o framework FastAPI, definindo rotas para consultar, criar e remover recursos, e validando os dados de entrada com modelos Pydantic.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota

#### Descrição
Abra o arquivo `starter-code.py`, crie a instância da aplicação `FastAPI` (se ainda não existir) e defina uma rota `GET /` que retorne uma mensagem de boas-vindas em formato JSON.

#### Requisitos
O programa concluído deve:

- Criar um objeto `app = FastAPI()`
- Definir a rota `GET /` com a função `home()`
- Retornar um dicionário como `{"message": "Bem-vindo à API de livros"}`
- Ser executado com `uvicorn starter-code:app --reload` e responder em `http://127.0.0.1:8000/`


### 🛠️ Buscar um Livro pelo ID

#### Descrição
Implemente a rota `GET /books/{book_id}`, que procura um livro na lista `BOOKS` pelo seu `id`. Se o livro não existir, a API deve responder com status `404`.

#### Requisitos
O programa concluído deve:

- Receber `book_id` como parâmetro de caminho do tipo `int`
- Retornar o livro encontrado em formato JSON
- Retornar erro `404` com a mensagem `"Livro não encontrado"` quando o `id` não existir

Exemplo de uso:

```text
GET /books/1  ->  200 {"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}
GET /books/99 ->  404 {"detail": "Livro não encontrado"}
```


### 🛠️ Cadastrar um Novo Livro com Validação

#### Descrição
Crie a rota `POST /books`, que recebe os dados de um novo livro no corpo da requisição (JSON), valida esses dados usando um modelo Pydantic e adiciona o livro à lista. O `id` do novo livro deve ser gerado automaticamente.

#### Requisitos
O programa concluído deve:

- Usar o modelo `BookCreate` (com `title`, `author` e `year`) para validar o corpo da requisição
- Gerar um `id` novo, igual ao maior `id` existente somado a 1
- Retornar o livro criado com status `201`
- Rejeitar automaticamente (status `422`) requisições em que `year` não seja um número inteiro ou em que `title` esteja vazio

Exemplo de corpo da requisição:

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```


### 🛠️ Remover um Livro e Filtrar por Autor

#### Descrição
Implemente duas rotas adicionais: `DELETE /books/{book_id}` para remover um livro e `GET /books` que lista os livros e aceita o parâmetro de consulta opcional `author` para filtrar os resultados.

#### Requisitos
O programa concluído deve:

- Remover o livro com o `id` informado e retornar `{"message": "Livro removido"}`
- Retornar `404` ao tentar remover um livro inexistente
- Na rota `GET /books`, retornar todos os livros quando `author` não for informado
- Na rota `GET /books?author=Machado de Assis`, retornar apenas os livros desse autor (sem diferenciar maiúsculas e minúsculas)
- Ao final, verificar a documentação interativa gerada automaticamente em `http://127.0.0.1:8000/docs`
