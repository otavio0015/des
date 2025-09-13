cont = soma = 0
numero = int(input('Digite numero ou [ 999 ] para sair: ')) 
while True:
    cont += 1
    soma += numero
    numero = int(input('Digite numero ou [ 999 ] para sair: ')) 
    if numero == 999:
        break
print(f'Foram digitados {cont} numeros e a soma entre eles é {soma}')

#concluido