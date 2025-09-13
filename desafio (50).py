#desenvolva um progama que leia seis numeros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidere-o.
soma = 0
conta = 0
for valor in range(1, 7, 1):
    numero = int(input(f'Digite {valor}° valor: '))
    if numero % 2 == 0:
        soma += numero
        conta += 1
print(f'Você informou {conta} numeros PARES e a soma deles é {soma}')

#concluido