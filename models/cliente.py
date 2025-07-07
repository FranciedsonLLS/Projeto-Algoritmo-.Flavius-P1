from funcs.validacao import validaCPF


def add_cliente(clientes):
    cadastrado = 0
    while(not(cadastrado)):
        cpf = input("CPF (123.456.789-09): ")
                # VALIDANDO CPF ]

        if(not(validaCPF(cpf))):
            print("CPF INVALIDO!!!")
            break
        if cpf in clientes:
            print("Cliente já cadastrado.")
            break
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        clientes[cpf] = {"nome": nome, "cpf": cpf, "endereco": endereco, "telefone": telefone}
        cadastrado = 1
        print(f"Cliente {nome} cadastrado com sucesso.")



def listar_clientes(clientes):
    print("\n--- Lista de Clientes ---")
    for c in clientes.values():
        print(f"Nome: {c['nome']}, CPF: {c['cpf']}, Endereço: {c['endereco']}, Telefone: {c['telefone']}")



def editar_cliente(clientes):
    cpf = input("CPF do cliente para editar: ")
    if cpf in clientes:
        cliente = clientes[cpf]
        cliente["nome"] = input(f"Novo nome ({cliente['nome']}): ") or cliente["nome"]
        cliente["endereco"] = input(f"Novo endereço ({cliente['endereco']}): ") or cliente["endereco"]
        cliente["telefone"] = input(f"Novo telefone ({cliente['telefone']}): ") or cliente["telefone"]
        print("Cliente atualizado com sucesso.")
                #logico anterior de ponteiro *(clientes[cpf]=cliente)
    else:
        print("Cliente não encontrado.")



def remover_cliente(clientes):
    cpf = input("CPF do cliente para remover: ")
    if cpf in clientes:
        removido = clientes.pop(cpf)
        print(f"Cliente {removido['nome']} removido.")
    else:
        print("Cliente não encontrado.")