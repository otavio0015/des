o = '=-' * 40
lista = []
print(o)
while True:
    numeros = input('Digite um valor: ')
    if numeros not in lista:
        lista.append(numeros)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    print(o)
    while True:
        continua = input('Quer continuar? [ S ] ou [ N ] ').upper()
        if continua in ['S', 'N']:
            break
        else:
            print('Opção invalida')
    print(o)
    if continua == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
print(o)

# concluido