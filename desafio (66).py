soma = cont = 0
while True:
    numeros = int(input('Digite o numero ou [ 999 ] para sair: '))
    if numeros == 999:
        break
    soma += numeros
    cont += 1
print(f'Você digitou {cont} numeros e soma entres os numero é igual a {soma}')

# concluido