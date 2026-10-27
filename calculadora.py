primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
operacao = input('Digite a operação desejada! \n+ para soma \n- para subtração \n* para multiplicação \n/ para divisão \n')

if operacao == '+':
    resultado = primeiro_numero + segundo_numero
    print(f'O resultado da soma é: {resultado}')
elif operacao == '-':
    resultado = primeiro_numero - segundo_numero
    print(f'O resultado da subtração é: {resultado}')
elif operacao == '*':
    resultado = primeiro_numero * segundo_numero
    print(f'O resultado da multiplicação é: {resultado}')
elif operacao == '/':
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
        print(f'O resultado da divisão é: {resultado}')
    else:
        print('Erro: Divisão por zero não é permitida.')
else:
    print('Operação inválida. Por favor, escolha uma operação válida.')
    