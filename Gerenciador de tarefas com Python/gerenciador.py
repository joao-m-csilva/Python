
def adicionar_tarefa(tarefas, nome_tarefa):

    #tarefa: nome da tarefa
    #completada: indicar se essa tarefa já foi completada
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

# ver_tarefas começando do 1 utilizando start
def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start= 1):
        status = "✔️" if tarefa["completada"] else "❌"
        nome_tarefa = tarefa["nome"]
        print(f"{indice} - [{status}] {nome_tarefa}")

# ver_tarefas utilizando indice + 1 (começando a partir do 1)
def ver_tarefas2(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✔️" if tarefa["completada"] else "❌"
        nome_tarefa = tarefa["nome"]
        print(f"{indice + 1} - [{status}] {nome_tarefa}")        
    return


def atualizar_tarefa(tarefas, indice, novo_nome):
    print(f"Tarefa {indice} atualizada para: {novo_nome}")
    return

def atualizar_nome_tarefa(tarefas, indice, novo_nome):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["nome"] = novo_nome
    else:
        print("Índice inválido.")
    return

def completar_tarefa(tarefas, indice):
    indice_ajustado = int(indice) - 1
    tarefas[indice_ajustado]["completada"] = True
    print(f"Tarefa {indice} marcada como completada")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas removidas com sucesso!")
    return

tarefas = []



while True:
    print("\nMenu do Gerenciador da Lista de Tarefas:")
    print("1 - Adicionar Tarefa")
    print("2 - Ver Tarefa")
    print("3 - Atualizar Tarefa")
    print("4 - Completar Tarefa")
    print("5 - Deletar Tarefas Completadas")
    print("6 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1": 
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)
        
    elif escolha == "3":
       
        ver_tarefas(tarefas) 
        indice = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice, novo_nome)
        atualizar_nome_tarefa(tarefas, indice, novo_nome)

    elif escolha == "4":
        indice = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice)
        
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)


    elif escolha == "6":
        break
print("Saindo do programa...") 
