cont = soma = maior = menor = 0
numeros = int(input('Digite numero ou [ 0 ] para sair: '))
while True:
    cont += 1
    soma += numeros
    if cont == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    numeros = int(input('Digite numero ou [ 0 ] para sair: '))
    if numeros == 0:
        break
media = soma / cont
print(f'Voce digitou {cont} e a media entre os numeros digitado é {media}')
print(f'O maior numero digitado foi {maior} e o menor {menor}')

# concluido