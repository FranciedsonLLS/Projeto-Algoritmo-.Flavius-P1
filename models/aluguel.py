from datetime import date
#alugueis, livros, clientes
def registrar_aluguel(alugueis, livros, clientes):
    # VERIFICA CLIENTE PELO CPF AGORA
    cpf = input("CPF do cliente: ")
    if cpf not in clientes:
        print("Cliente não encontrado.")
        return
    # VERIFICA LIVRO PELO NOME
    nome_livro = input("Nome do livro: ")
    if nome_livro not in livros:
        print("Livro não encontrado.")
        return
    #PONTEIRO
    livro = livros[nome_livro]
    if livro["quantidade"] <= 0:
        print("Livro fora de estoque.")
        return
    # RETIRANDO DO ESTOQUE 
    livro["quantidade"] -= 1
    alugueis[len(alugueis)+1] = {
        "cliente_cpf": cpf,
        "livro_nome": nome_livro,
        "data": str(date.today()),
        "status": "pendente"
    }
    print(f"Aluguel registrado com ID #{len(alugueis)}")
    

def listar_alugueis(alugueis, clientes):
    if not alugueis:
        print("Nenhum aluguel registrado.")
        return
    print("\n--- Lista de Aluguéis ---")
    #.items retorno uma tupla para visualizacao
    for id, a in alugueis.items():
        cliente = clientes[a["cliente_cpf"]]["nome"]
        print(f"{id}. Cliente: {cliente}, Livro: {a['livro_nome']}, Data: {a['data']}, Status: {a['status']}")




def registrar_devolucao(alugueis, historico, clientes):
    # perguntar no "nome" quem vai registrar a devolucao 
    cpf = input("CPF do cliente: ")
    if cpf not in clientes:
        print("Cliente não encontrado.")
        return
    
    print("Alugueis pendentes: ")
    for id, a in alugueis.items():
        cliente = clientes[a["cliente_cpf"]]["nome"]
        if(a["cliente_cpf"]==cpf):
            print(f"{id}. Cliente: {cliente}, Livro: {a['livro_nome']}, Data: {a['data']}, Status: {a['status']}")
    
    id_remover = int(input("Informe o ID do aluguel a registrado como devolvido: "))
    aluguel_remover = alugueis[id_remover]
    historico[len(historico)+1] = {
        "cliente_cpf": cpf,
        "livro_nome": aluguel_remover["livro_nome"],
        "data": aluguel_remover['data'],
        "status": "Devolvido",
        "data_devolveu": str(date.today())
    }
    alugueis.pop(id_remover)


#lista de historico
def lista_historico(historico):
    print("\n--- Historico ---")
    if(len(historico)==0):
        print("Nenhum livro foi devolvido!!")
    else:
        for l in historico.values():
            print(f"CPF: {l['cliente_cpf']}, LIVRO: {l['livro_nome']}, Data do Aluguel: {l['data']}, status: {l['status']}, Devolucao: {l['data_devolveu']}")