def adicionar_tarefa(tarefas, nome_tarefa):

    #tarefa: nome da tarefa
    #status: indica se já foi completada ou não
    tarefa = {"nome": nome_tarefa, "status": False}
    tarefas.append(tarefa)
    print(f'A tarefa {tarefa["nome"]} foi adicionada com sucesso!')
    return 

def ver_tarefas(tarefas):
    print('\nLista de tarefas.')
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["status"] == True else " "
        nome_tarefa = tarefa["nome"]
        print(f'{indice}. [{status}] {nome_tarefa}')
    return

def atualizar_tarefas(tarefas, numero_tarefa, novo_nome):
    indice_tarefa_ajustado = int(numero_tarefa)-1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome
        print(f'Tarefa {numero_tarefa} atualizada para {novo_nome}')
    else:
        print('Indice de tarefa inválido.')
    return

def completar_tarefa(tarefas, numero_tarefa):
    indice_tarefa_ajustado = int(numero_tarefa)-1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefa_completada = tarefas[indice_tarefa_ajustado]["status"] = True
        tarefa_nome = tarefas[indice_tarefa_ajustado]["nome"]
        print(f'A tarefa {tarefa_nome} foi atualizada.')
    else:
        print('Indice de tarefa inválido.')
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["status"] == True:
            tarefas.remove(tarefa)
    print('Tarefas completadas deletadas.')
    return

tarefas = []
while True:
    print('\nMenu do Gerenciador de Listas de Tarefas:')
    print('1. Adicionar tarefas.')
    print('2. Ver tarefas.')
    print('3. Atualizar tarefas.')
    print('4. Completar tarefas.')
    print('5. Deletar tarefas.')
    print('6. Sair')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == '2':
        ver_tarefas(tarefas)
    elif escolha == '3':
        ver_tarefas(tarefas)
        numero_tarefa = input('Digite o número da tarefa a ser atualizada: ')
        novo_nome = input('Digite o novo nome para a tarefa: ')
        atualizar_tarefas(tarefas, numero_tarefa, novo_nome)
    elif escolha == '4':
        ver_tarefas(tarefas)
        numero_tarefa = input('Digite o número da tarefa que deseja completar: ')
        completar_tarefa(tarefas, numero_tarefa)
    elif escolha =='5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == '6':
        break

print('Programa finalizado.')