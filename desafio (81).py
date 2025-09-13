lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    while True:
        continuar = input('Continuar? [S/N] ').upper()
        if continuar in ['N', 'S']:
            break
        elif continuar not in ['N', 'S']:
            print('Opção invalida')
    if continuar == 'N':
        break

if 5 in lista:
    na_lista = 'está'
else:
    na_lista = 'não está'

lista.sort(reverse=True)

print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5 {na_lista} na lista')