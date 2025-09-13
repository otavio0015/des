lista = [[], [], []]
soma_pares= soma_3 = 0
for c in range(3):
    num1 = int(input(f'Digite um valor para [0, {c}]: '))
    lista[0].append(num1)
    if num1 %2 == 0:
        soma_pares += num1
for d in range(3):
    num2 = int(input(f'Digite um valor para [1, {d}]: '))
    lista[1].append(num2)
    if num2 %2 == 0:
        soma_pares += num2
for e in range(3):
    num3 = int(input(f'Digite um valor para [2, {e}]: '))
    lista[2].append(num3)
soma_3 = lista[0][2] + lista[1][2] + lista[2][2]
print('=' * 50)
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
print('=' * 50)
print(f'O soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_3}')
print(f'O maior valor da segunda linha é {max(lista[1])}')

# concluido
