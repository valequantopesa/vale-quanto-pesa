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


'''
def busca_ativo_carteira(ativo):
    db, carteira = conecta_carteira()
    return db.carteira.find_one(ativo)


def busca_todos_dados_ativos_carteira():
    db, carteira = conecta_carteira()
    return db.carteira.find()


def atualiza_carteira(id, dados, **kwargs):
    db, carteira = conecta_carteira()
    db.carteira.update(
        id, dados,
        upsert=kwargs.get('upsert', False))


def adiciona_na_carteira(ativo, valor, qntd_compra, data):
    db_carteira, carteira = conecta_carteira()
    dados_carteira = {
        'ativo': ativo,
        'dados': {
            'compra': [[valor, qntd_compra, data]],
            'venda': [],
            'quantidade_comprado': qntd_compra,
            'quantidade_vendido': 0,
        },
    }
    id = carteira.insert_one(dados_carteira).inserted_id

# ------------------------------------------------------------------


def conecta():
    db = cliente.ativos
    ativos = db.ativos
    return db, ativos


def inserir(db, ativos, dados):
    id = ativos.insert_one(dados).inserted_id


def atualiza(ativo, valor, **kwargs):
    db, ativos = conecta()
    db.ativos.update(
        ativo, valor,
        upsert=kwargs.get('upsert', False))


def busca_ativo(ativo):
    db, ativos = conecta()
    return db.ativos.find_one(ativo)

def remove_ativo(ativo):
    db, ativos = conecta()
    db.ativos.remove(ativo)
    
def busca_todos_ativos():
    db, ativos = conecta()
    return db.ativos.find({}, {'ativo'})


def busca_todos_relatorios_finais():
    db, ativos = conecta()
    return db.ativos.find({}, {'relatorio_fim_expediente'})


def adiciona_ativo_json_status_invest(ativo):
    db, ativos = conecta()
    for num in ['1', '2']:
        resposta_api = session.get(
            URL_BUSCA_API_ATIVOS_STATUS_INVEST.format(num))
        ativos_json = json.loads(resposta_api.content)
        for dado_json in ativos_json:
            if dado_json['ticker'] != ativo:
                continue

            dados = {
                'ativo': dado_json['ticker'],
                'empresa': dado_json['companyName'],
                'data_valor_variacao': {
                },
                'relatorio_fim_expediente': {
                },
                'data_valor_atual': {
                },
                'valor_atual': {
                },
                'variacao_valor_atual': {
                },
                'data_cricao_ativo': str(datetime.date.today())
            }
            inserir(db, ativos, dados)
            break


def itera_json_status_invest(db, ativos):
    for num in ['1', '2']:
        resposta_api = session.get(
            URL_BUSCA_API_ATIVOS_STATUS_INVEST.format(num))

        ativos_json = json.loads(resposta_api.content)
        for dado_json in ativos_json:
            dados = {
                'ativo': dado_json['ticker'],
                'empresa': dado_json['companyName'],
                'data_valor_variacao': {
                },
                'relatorio_fim_expediente': {
                }
            }
            inserir(db, ativos, dados)


def itera_csv(db, ativos):
    with open('empresa_ativos.csv', 'rb') as csv_ativos:
        file = csv.reader(csv_ativos, delimiter=',', quotechar='|')
        for row in file:
            if row[0] == '':
                continue

            empresa = row.pop(0)
            for nomo_ativo in [item for item in row if item != '']:
                dados = {
                    'ativo': nomo_ativo,
                    'empresa': empresa,
                    'data_valor_variacao': {
                    },
                    'relatorio_fim_expediente': {
                    }
                }
                inserir(db, ativos, dados)
'''
if __name__ == '__main__':
    pass
