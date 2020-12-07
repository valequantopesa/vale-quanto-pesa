#!/usr/local/bin/python3
# encoding: utf-8

import pdb
from pymongo import MongoClient
import datetime

cliente = MongoClient('localhost', 27017)


def conecta():
    db_vale_quanto_pesa = cliente.vale_quanto_pesa
    produto = db_vale_quanto_pesa.produto
    return db_vale_quanto_pesa, produto


def insere(dados_produto):
    db_vale_quanto_pesa, produto = conecta()
    id = produto.insert_one(dados_produto).inserted_id
    return


def busca():
    db_vale_quanto_pesa, produto = conecta()
    return db_vale_quanto_pesa.produto.find()


def busca_alimento(nome_alimento):
    db_vale_quanto_pesa, produto = conecta()
    return db_vale_quanto_pesa.produto.find_one(
        {'nome_alimento': nome_alimento})

if __name__ == '__main__':
    pass
