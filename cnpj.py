import re
import random

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida_entrada(cnpj):
    cnpj = remover_caracteres(cnpj)

    try:
        if sequencia(cnpj):
            print('É uma sequência')
            return False
    except:
        return False

    novo_cnpj = cnpj[:-2]
    if valida_cnpj(novo_cnpj, cnpj):
        return True
    return False


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def sequencia(cnpj):
    seq = cnpj[0] * len(cnpj)
    if seq == cnpj:
        return True

    return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivo = REGRESSIVOS[1:]
    elif digito == 2:
        regressivo = REGRESSIVOS
    else:
        return None

    soma = 0
    for i, regressivo in enumerate(regressivo):
        soma += int(cnpj[i]) * regressivo

    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    cnpj += str(digito)

    return cnpj


def valida_cnpj(novo_cnpj, cnpj):
    try:
        novo_cnpj = calcula_digito(novo_cnpj, 1)
        novo_cnpj = calcula_digito(novo_cnpj, 2)
    except:
        return False

    if novo_cnpj == cnpj:
        return True
    return False

def gera():
    primeiro_digito=random.randint(0,9)
    segundo_digito=random.randint(0,9)
    segundo_bloco=random.randint(100,999)
    terceiro_bloco=random.randint(100,999)
    quarto_bloco='0001'

    inicio_cnpj=f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}'
    novo_cnpj=calcula_digito(inicio_cnpj,1)
    novo_cnpj=calcula_digito(novo_cnpj,2)
    return novo_cnpj

def formata(cnpj):
    cnpj=remover_caracteres(cnpj)
    formatada=f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatada