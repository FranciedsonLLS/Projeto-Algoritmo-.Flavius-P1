

def add_livro(livros):
    cadastrado = 0
    while(not(cadastrado)):
        nome = input("Nome do livro: ")
        if nome in livros:
            print("Livro já cadastrado.")
            break
        tema = input("Tema: ")
        autor = input("Autor: ")
        quantidade = int(input("Quantidade: "))
        #ADD TRATAMENTO!!!! ################
        livros[nome] = {"nome": nome, "tema": tema, "autor": autor, "quantidade": quantidade}
        cadastrado = 1
        print("Livro cadastrado com sucesso.")


def listar_livros(livros):
    print("\n--- Lista de Livros ---")
    if(len(livros)==0):
        print("Nenhum Livro Registrado!!!")
    else:
        for l in livros.values():
            print(f"Nome: {l['nome']}, Tema: {l['tema']}, Autor: {l['autor']}, Quantidade: {l['quantidade']}")


def editar_livro(livros):
    verificar = 1
    while(verificar):
        nome = input("Nome do livro para editar: ")
        if nome in livros:
            livro = livros[nome]
            nova_qtd = input(f"Nova quantidade ({livro['quantidade']}): ")
            if (nova_qtd.isdigit()):
                print("Quantidade Aceita!")
            else:
                print("A quantidade a ser atualizada é inválida")
                break
            livro["nome"] = input(f"Novo nome ({livro['nome']}): ") or livro["nome"]
            livro["tema"] = input(f"Novo tema ({livro['tema']}): ") or livro["tema"]
            livro["autor"] = input(f"Novo autor ({livro['autor']}): ") or livro["autor"]
            livro["quantidade"] = int(nova_qtd)
            verificar = 0
            print(f"O livro foi alterado para Nome: {livro['nome']} / Tema: {livro['tema']} / Autor: {livro['autor']}")
        else:
            print(f"O Livro {nome} não existe no estoque!!")
            verificar = 0

def remover_livro(livros):
    nome = input("Nome do livro para remover: ")
    if nome in livros:
        op = input(f"Tem certeza que quer remover o livro: {nome}? s/n:   ")
        if(op=='s'):
            livros.pop(nome)
            print(f"Livro '{nome}' removido.")
        else:
            print("Remoção Cancelada!!!")
    else:
        print("Livro não encontrado.")
