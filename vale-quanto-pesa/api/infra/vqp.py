#!/usr/local/bin/python3
# encoding: utf-8

import pdb
import datetime
import time
import click

import sys
sys.path.append('../')

from dao.db import insere

DEBUG = False

PRODUTO = {
    'nome_alimento': '',
    'ingredientes': [],
    'etapas': {
        'etapa_1': '',
        'etapa_2': ''
    },
    'origem': {
        'animal': None,
        'vegetal': None,
        'mineral': None
    },
    'dependencias': {
        'produdo': 1
    },
    'similares': {
        'produto': 1
    },
    'producao': {
        'industrializado': None,
        'natural': None,
        'indefinido': None
    },
    'embalagem': {
        'plastico': None,
        'papel': None
    },
    'conservacao': {
        'baixa_temperatura': None,
        'temperatura_ambiente': None
    },
    'valores': {
        'valor_medio_vendido': None,
        'valor_baseado_em_produtos': None
    },
    'fontes': []

}


def adiciona():
    id = insere(PRODUTO)

def adiciona_produto(produto):
    PRODUTO.update({'nome_alimento':produto.nome_alimento})
    PRODUTO.update({'ingredientes':produto.ingredientes})
    PRODUTO.update({'etapas':produto.etapas})
    PRODUTO.update({'origem':produto.origem})
    PRODUTO.update({'dependencias':produto.dependencias})
    PRODUTO.update({'similares':produto.similares})
    PRODUTO.update({'producao':produto.producao})
    PRODUTO.update({'embalagem':produto.embalagem})
    PRODUTO.update({'conservacao':produto.conservacao})
    PRODUTO.update({'valores':produto.valores})
    PRODUTO.update({'fontes':produto.fontes})
    insere(PRODUTO)
    return 'ok'

@click.command()
@click.option('-ad', '--adiciona_produto', is_flag=True,
              help='Adiciona ativo no banco.')
def executar(adiciona_produto):
    if adiciona_produto:
        adiciona()
    else:
        print('Nada selecionado')


if __name__ == '__main__':
    executar()
