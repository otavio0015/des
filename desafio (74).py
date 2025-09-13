from random import randint
print('Os valores sorteados foram:', end=' ')
lista = []
for c in range(5):
    numero = randint(0, 10)
    lista.append(numero)
    print(numero, end=' ')
print(f'\nO maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')

# concluido