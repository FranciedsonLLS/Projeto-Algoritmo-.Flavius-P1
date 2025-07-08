# funcs/bds.py
import json
import os

#carrego dado x
def carregar_arquivo(caminho):
    if os.path.exists(caminho):
        with open(caminho, "r") as arquivo:
            return json.load(arquivo)
    return {}
#salva dado x
def salvar_arquivo(dados, caminho):
    with open(caminho, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

# MAIN CARREGA DADOS
def carregar_bd():
    return {
        "clientes": carregar_arquivo("clientes.txt"),
        "livros": carregar_arquivo("livros.txt"),
        "alugueis": carregar_arquivo("alugueis.txt"),
        "historico": carregar_arquivo("historico.txt")
    }

# Função central para salva 
def salvar_bd(clientes, livros, alugueis, historico):
    salvar_arquivo(clientes, "clientes.txt")
    salvar_arquivo(livros, "livros.txt")
    salvar_arquivo(alugueis, "alugueis.txt")
    salvar_arquivo(historico, "historico.txt")
