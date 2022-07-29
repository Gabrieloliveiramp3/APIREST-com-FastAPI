from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
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

@app.get('/movies/{movies_id}')
def procurar_filmes(movies_id: str):
    for movie in banco:
        if movie.Id == movies_id:
            return movie

@app.delete('/movies/{movies_id}')
def remover_filmes(movies_id: str):
    posicao = -1
    #Busca a posição do filme
    for index, movie in enumerate(banco):
        if movie.Id == movies_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'Filme removido com sucesso'}
    else:
        return {'Filme não localizado'}

@app.post("/movies")
def cadastrar_filmes(filme: Movies):
    banco.append(filme)
    #uuid4 gera o id automaticamente
    filme.Id = str(uuid4())
    return {f"Filme {filme.Titulo} cadastrado com sucesso!"}

#rodar o programa, digitar isso no terminal : uvicorn main:app --reload
#http://127.0.0.1:8000/docs quando coloca docs, vai para uma pagina mais interativa e também tem o redoc