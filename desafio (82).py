lista = []
par = []
impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor %2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    while True:
        continuar = input('Continuar? [S/N] ').upper()
        if continuar in ['N', 'S']:
            break
        elif continuar not in ['N', 'S']:
            print('Opção invalida')
    if continuar == 'N':
        break

print('-=' * 40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
