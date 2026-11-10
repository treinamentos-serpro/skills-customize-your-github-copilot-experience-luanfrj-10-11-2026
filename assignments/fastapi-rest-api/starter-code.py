from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Dados iniciais (em memória). Não há banco de dados nesta atividade.
BOOKS = [
    {"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 2, "title": "Memórias Póstumas de Brás Cubas", "author": "Machado de Assis", "year": 1881},
    {"id": 3, "title": "O Cortiço", "author": "Aluísio Azevedo", "year": 1890},
]

# Sua aplicação começa aqui: crie o app e as rotas abaixo.
