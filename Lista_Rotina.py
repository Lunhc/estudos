# Lista de Rotina - projeto simples
# O programa mostra um menu e repete até você escolher 'sair'.
# Cada tarefa é um dicionário com duas informações: nome e feita.

tarefas = []  # lista vazia que vai guardar as tarefas


def mostrar_menu():
    print('\n=== LISTA DE ROTINA ===')
    print('1 - Adicionar tarefa')
    print('2 - Ver tarefas')
    print('3 - Marcar tarefa como feita')
    print('4 - Remover tarefa')
    print('5 - Sair')


def ler_numero(mensagem):
    """Pede um número ao usuário; retorna None se não for um número válido."""
    try:
        return int(input(mensagem))
    except ValueError:
        return None


def adicionar_tarefa():
    nome = input('Digite o nome da tarefa: ')
    tarefa = {'nome': nome, 'feita': False}
    tarefas.append(tarefa)  # adiciona no final da lista
    print('Tarefa adicionada com sucesso!')


def ver_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa na lista.')
        return  # sai da função

    print('\nSuas tarefas:')
    # enumerate dá o número (posição) e a tarefa; start=1 começa a contagem em 1
    for numero, tarefa in enumerate(tarefas, start=1):
        if tarefa['feita']:
            status = '[x]'
        else:
            status = '[ ]'
        print(f'{numero}. {tarefa["nome"]} - {status}')


def marcar_como_feita():
    ver_tarefas()
    if len(tarefas) == 0:
        return

    numero = ler_numero('Número da tarefa concluída: ')
    if numero is not None and 1 <= numero <= len(tarefas):
        tarefas[numero - 1]['feita'] = True
        print('Parabéns! Você concluiu a tarefa.')
    else:
        print('Número inválido. Tente novamente.')


def remover_tarefa():
    ver_tarefas()
    if len(tarefas) == 0:
        return

    numero = ler_numero('Número da tarefa a ser removida: ')
    if numero is not None and 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print('Tarefa removida com sucesso!')
    else:
        print('Número inválido. Tente novamente.')


# ---------------- Programa principal ----------------
while True:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        adicionar_tarefa()
    elif opcao == '2':
        ver_tarefas()
    elif opcao == '3':
        marcar_como_feita()
    elif opcao == '4':
        remover_tarefa()
    elif opcao == '5':
        print('Até logo!')
        break
    else:
        print('Opção inválida. Tente novamente.')