from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movies(BaseModel):
    Id: int
    Titulo: str
    Descricao: str
    Autor: str

banco: List[Movies] = []

@app.get("/")
def home():
    return 'Olá, aqui é um teste de APIREST'

@app.get('/movies')
def listar_filmes():
    return banco

@app.post("/cadmovies")
def cadastrar_filmes(filme: Movies):
    banco.append(filme)
    return {f"Filme {filme.Titulo} cadastrado com sucesso!"}

#rodar o programa, digitar isso no terminal : uvicorn main:app --reload
#http://127.0.0.1:8000/docs quando coloca docs, vai para uma pagina mais interativa e também tem o redoc