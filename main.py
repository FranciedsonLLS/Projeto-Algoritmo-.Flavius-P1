def exibir_menu():
    print("\n=== MENU BIBLIOTECA PESSOAL ===")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Livros")
    print("3. Registrar Venda/Aluguel")
    print("4. Gerenciar Estoque")
    print("5. Sair")

def menu_clientes():
    print("\n--- MENU CLIENTES ---")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Editar Cliente")
    print("4. Remover Cliente")
    print("5. Voltar")

def menu_livros():
    print("\n--- MENU LIVROS ---")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Editar Livro")
    print("4. Remover Livro")
    print("5. Voltar")

def menu_transacoes():
    print("\n--- MENU VENDAS/ALUGUÉIS ---")
    print("1. Registrar Venda")
    print("2. Registrar Aluguel")
    print("3. Listar Transações")
    print("4. Voltar")

def menu_estoque():
    print("\n--- MENU ESTOQUE ---")
    print("1. Adicionar Estoque de Livro")
    print("2. Ver Estoque Atual")
    print("3. Ajustar Quantidade")
    print("4. Voltar")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            menu_transacoes()
        elif opcao == "4":
            menu_estoque()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
