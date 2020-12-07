#!/usr/local/bin/python3
# encoding: utf-8

import pdb
import sys
from fastapi import FastAPI, Form
from starlette.responses import HTMLResponse
from typing import List

#sys.path.append('../')
from models.model import Produto
from dao.db import busca, busca_alimento
from infra.vqp import adiciona_produto

app = FastAPI()

@app.get('/produtos')
async def produtos():
    alimentos = []
    for produto in busca():
        alimentos.append(Produto(**produto))
    return {'alimento': alimentos}

@app.get('/produto/{nome_alimento}')
async def produto_nome(nome_alimento):
    produto = busca_alimento(nome_alimento)
    return Produto(**produto)

@app.get("/form", response_class=HTMLResponse)
def form_get():
    return '''<form method="post"> 
    <input type="text" name="no" value="1"/> 
    <input type="text" name="nm" value="abcd"/> 
    <input type="submit"/> 
    </form>'''
     
@app.post("/novo/produto/")
async def novo_produto(produto: Produto):
    return adiciona_produto(produto)
        
if __name__ == '__main__':
    pass
