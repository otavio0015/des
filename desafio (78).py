lista = []
for c in range(5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=' * 40)
maior = lista.index(max(lista))
menor = lista.index(min(lista))
print(f'Voce digitou os valores {lista}')  
print(f'O maior valor digitado foi {max(lista)} nas posições {maior}...')
print(f'O menor valor digitado foi {min(lista)} nas posições {menor}...')