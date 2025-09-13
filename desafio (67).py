print('=' * 10)
print('Tabuada')
while True:
    print('=' * 10)
    numero = int(input('Digite um numero para tabuada: '))
    if numero < 0:
        break
    print('=' * 10)
    for c in range(10):
        print(f'| {numero} x {c} = {numero * c}')
print('=' * 9)
print('|  FIM  |')
print('=' * 9)

# concluido