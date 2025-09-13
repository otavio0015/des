lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    lista.append([nome, [nota1, nota2], media])

    continuar = input('Continuar? [S/N]: ')
    if continuar in 'Nn':
        break
print('-' * 40)
print(f'{'Nº':<4}{'Nome':<10}{'Media':>8}')
print('=' * 40)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('=' * 40)

while True:
    opcao = int(input('Mostrar notas de qual aluno? [999] interrompe: '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(lista) - 1:
        print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')

# concluido
