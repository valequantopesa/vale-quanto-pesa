#!/usr/local/bin/python3
# encoding: utf-8

import pdb
import sys
from fastapi import FastAPI

sys.path.append('../')
from models.model import Produto
from dao.db import busca

app = FastAPI()

@app.get('/produto')
async def produto():
    alimentos = []
    for produto in busca():
        alimentos.append(Produto(**produto))
    return {'alimento': alimentos}

'''
@app.get('/ativos/pagina/{pagina}')
async def ativos(pagina: int):
    ativos = []
    ativos_buscado = db_ativo.ativos.find().sort("ativo", 1
        ).skip(pagina * 10).limit(10)
    for ativo in ativos_buscado:
        ativos.append(Ativos(**ativo))
    return {'ativos': ativos}


@app.get('/estatistica/valorizados')
async def ativo_valorizados():
    lista_valorizados = []
    for ativo in valorizados():
        lista_valorizados.append(Estatistica(**ativo))
    return {'ativos_valorizados': lista_valorizados}

@app.get('/estatistica/valorIdeal')
async def valor_ideal():
    lista_valor_ideal = []
    for ativo in valor_ideal_venda():
        lista_valor_ideal.append(EstatisticaValorIdeal(**ativo))
    return {'valor_ideal': lista_valor_ideal}
'''
if __name__ == '__main__':
    pass
