# 📘 Atividade: Fundamentos de HTTP e JSON

## 🎯 Objetivo

Compreenda como uma API REST representa dados em JSON e organiza requisições e respostas usando métodos HTTP, caminhos e códigos de status. Antes de usar um framework, você vai simular operações de leitura e cadastro em uma pequena API de clubes escolares.

## 📝 Tarefas

### 🛠️ Ler e Criar Dados JSON

#### Descrição
Use o módulo `json` para transformar uma string JSON em dados Python e, depois, serializar um dicionário Python como JSON.

#### Requisitos
O programa concluído deve:

- Converter com `json.loads()` uma string que contenha `name` e `activity`
- Acessar e exibir os valores desses campos
- Criar um dicionário de resposta e convertê-lo em uma string JSON com `json.dumps()`

Exemplo de entrada:

```json
{"name": "Clube de Robótica", "activity": "Construção de robôs"}
```

### 🛠️ Simular Requisições GET

#### Descrição
Crie uma função `handle_request(method, path)` para simular a leitura de clubes. A função deve representar a resposta como um par com o código de status HTTP e o corpo JSON (um dicionário Python).

#### Requisitos
O programa concluído deve:

- Guardar ao menos dois clubes em uma lista de dicionários, cada um com `id` e `name`
- Retornar todos os clubes com status `200` para `GET /clubs`
- Retornar um clube com status `200` para `GET /clubs/{club_id}` quando o ID existir
- Retornar status `404` e uma mensagem de erro quando o clube não existir

### 🛠️ Simular o Cadastro com POST

#### Descrição
Amplie `handle_request` para aceitar também um corpo JSON e cadastrar um clube usando `POST /clubs`.

#### Requisitos
O programa concluído deve:

- Receber o corpo da requisição como uma string JSON e convertê-lo em dados Python
- Exigir o campo `name` com um valor não vazio
- Criar um ID para o novo clube e adicioná-lo à lista
- Retornar o clube criado com status `201`, ou status `400` quando o campo `name` estiver ausente ou vazio

