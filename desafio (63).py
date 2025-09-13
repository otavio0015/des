print('Sequencia de Fibonacci')
num = int(input('Quantos termos você que mostrar? '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' -> FIM')

#concluido