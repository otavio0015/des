#faca um progama que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for numero in range(1, 501):
    if numero % 3 ==0 and numero % 2 != 0:
        soma += numero
        cont += 1
print(f'A soma é de {cont} valores é {soma}')

#concluido
