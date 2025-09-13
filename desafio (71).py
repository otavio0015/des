print('=' * 30)
print('        Banco do Tavão')
print('=' * 30)
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Que valor você quer sacar? R$'))

if valor >= 50:
    cont50 = valor //50
    valor %= 50

if valor >= 20:
    cont20 = valor //20
    valor %= 20

if valor >= 10:
    cont10 = valor // 10
    valor %= 20

if valor >= 1:
    cont1 = valor // 1
    valor %= 1

if cont50 >= 1:
    print(f'Total de {cont50} cedulas de R$50.00')
if cont1 >= 1:
    print(f'Total de {cont20} cedulas de R$20.00')
if cont10 >= 1:
    print(f'Total de {cont10} cedulas de R$10.00')
if cont20 >= 1:
    print(f'Total de {cont1} cedulas de R$1.00')
print('=' * 30)
print('Volte sempre no banco do Tavão')
print('=' * 30)
# concluido