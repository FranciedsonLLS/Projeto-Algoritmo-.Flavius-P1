#imports
from datetime import date
from funcs.validacao import validaCPF
from models.cliente import remover_cliente, editar_cliente, listar_clientes, add_cliente
from models.livro import add_livro, listar_livros, editar_livro, remover_livro
from models.aluguel import registrar_aluguel, listar_alugueis, registrar_devolucao, lista_historico #alterar funcs dps
import os


clientes = {
    "123.456.789-00": {
        "nome": "Alice Martins",
        "cpf": "123.456.789-00",
        "endereco": "Rua das Flores, 123",
        "telefone": "(11) 91234-5678"
    },
    "987.654.321-00": {
        "nome": "Bruno Silva",
        "cpf": "987.654.321-00",
        "endereco": "Av. Paulista, 456",
        "telefone": "(11) 99876-5432"
    },
    "111.222.333-44": {
        "nome": "Carla Souza",
        "cpf": "111.222.333-44",
        "endereco": "Rua do Sol, 789",
        "telefone": "(21) 91234-4321"
    },
    "555.666.777-88": {
        "nome": "Diego Ramos",
        "cpf": "555.666.777-88",
        "endereco": "Travessa da Serra, 101",
        "telefone": "(31) 98765-4321"
    },
    "999.888.777-66": {
        "nome": "Eduarda Lima",
        "cpf": "999.888.777-66",
        "endereco": "Rua Verde, 202",
        "telefone": "(71) 99988-7766"
    }
}

livros = {
    "1984": {
        "nome": "1984",
        "tema": "Distopia",
        "autor": "George Orwell",
        "quantidade": 3
    },
    "Dom Casmurro": {
        "nome": "Dom Casmurro",
        "tema": "Romance",
        "autor": "Machado de Assis",
        "quantidade": 5
    },
    "O Hobbit": {
        "nome": "O Hobbit",
        "tema": "Fantasia",
        "autor": "J.R.R. Tolkien",
        "quantidade": 2
    },
    "A Revolução dos Bichos": {
        "nome": "A Revolução dos Bichos",
        "tema": "Satírico/Político",
        "autor": "George Orwell",
        "quantidade": 4
    },
    "Memórias Póstumas de Brás Cubas": {
        "nome": "Memórias Póstumas de Brás Cubas",
        "tema": "Romance Filosófico",
        "autor": "Machado de Assis",
        "quantidade": 1
    }
}
    # chave: NOME  ////// tirar chave de nome
from datetime import date

alugueis = {
    1: {
        "cliente_cpf": "123.456.789-00",
        "livro_nome": "1984",
        "data": str(date(2025, 7, 1)),
        "status": "pendente"
    },
    2: {
        "cliente_cpf": "987.654.321-00",
        "livro_nome": "Dom Casmurro",
        "data": str(date(2025, 6, 28)),
        "status": "pendente"
    },
    3: {
        "cliente_cpf": "111.222.333-44",
        "livro_nome": "O Hobbit",
        "data": str(date(2025, 7, 3)),
        "status": "pendente"
    },
    4: {
        "cliente_cpf": "123.456.789-00",
        "livro_nome": "O Hobbit",
        "data": str(date(2025, 7, 3)),
        "status": "pendente"
    }
    
}

  # chave: ID
historico = {} #chave: ID
# historico = [] add depois

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

# LISTAR ALUGUEL

# MAIN
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            #request #alugueis, livros e clientes
            menu_alugueis()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
