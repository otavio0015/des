posicao = 0
primeiro = int(input('Digite um numero: '))
segundo = int(input('Digite outro numero: '))
terceiro = int(input('Digite mais um numero: '))
quarto = int(input('Digite o ultimo numero: '))
lista = primeiro, segundo, terceiro, quarto
if 9 in lista:
    print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 aparece na {lista.index(3)+1}º posição')
print(f'Os valores par digitados foram: ',end='')
for n in lista:
    if n %2 == 0:
        print(n, end=' ')
# concluido