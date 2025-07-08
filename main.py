#imports
from datetime import date
from funcs.validacao import validaCPF
from models.cliente import remover_cliente, editar_cliente, listar_clientes, add_cliente
from models.livro import add_livro, listar_livros, editar_livro, remover_livro
from models.aluguel import registrar_aluguel, listar_alugueis, registrar_devolucao, lista_historico #alterar funcs dps
from funcs.bds import carregar_bd, salvar_bd
import json
import os


#MENU
def exibir_menu():
    print("\n===\ MENU BIBLIOTECA PESSOAL /===")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Livros")
    print("3. Gerenciar Alugueis")
    print("4. Sair")

# CLIENTES
def menu_clientes():
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("4. Remover Cliente")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        #CADASTRAR CLIENTE
        if opcao == "1":
            add_cliente(clientes)
        #LISTA CLIENTE
        elif opcao == "2":
            listar_clientes(clientes)
        #LISTAR CLIENTES
        elif opcao == "3":
            editar_cliente(clientes)
        #REMOVER CLIENTE PELO CPF(chave)
        elif opcao == "4":
            remover_cliente(clientes)

        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# LIVROS
def menu_livros():
    while True:
        
        print("\n--- MENU LIVROS ---")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Editar Livro")
        print("4. Remover Livro")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        #REGISTRAR LIVRO
        if opcao == "1":
            add_livro(livros)
        #LISTAR LIVROS
        elif opcao == "2":
            listar_livros(livros)
        #EDITAR LIVRO
        elif opcao == "3":
            editar_livro(livros)
        #REMOVER LIVRO
        elif opcao == "4":
            remover_livro(livros)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# MENU DE ALUGUEL

def menu_alugueis():
    while True:
        
        print("\n--- MENU ALUGUEIS ---")
        print("1. Registrar Aluguel")
        print("2. Listar Alguel")
        print("3. Registrar Devolução")
        print("4. Exibir Historico de Alugueis")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        #REGISTRAR LIVRO
        if opcao == "1":
            ##alugueis, livros, clientes
            registrar_aluguel(alugueis, livros, clientes)
        #LISTAR LIVROS
        elif opcao == "2":
            #alugueis, clientes
            listar_alugueis(alugueis, clientes)
        #EDITAR LIVRO
        elif opcao == "3":
            #
            registrar_devolucao(alugueis, historico, clientes)
        #REMOVER LIVRO
        elif opcao == "4":
            lista_historico(historico)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# CARREGAR DICIONARIOS

# MAIN
def main():
    #variaveis globais momentaneas dentro do codigo
    global clientes, livros, alugueis, historico
    #carrega os dados dos arquivos
    bd = carregar_bd()
    #atribuindo os bds de cada txt nos dic do codigo
    clientes = bd["clientes"]
    livros = bd["livros"]
    alugueis = bd["alugueis"]
    historico = bd["historico"]

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            menu_alugueis()
        elif opcao == "4":
            print("Encerrando o programa e salvando os dados!!!")
            # Salvando os dados dos dic do codigos para os txts
            salvar_bd(clientes, livros, alugueis, historico)
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
