#faça um progama que leia um numero inteiro e diga se ele é ou não um numero primo.
num = int(input('Digite o numero: '))
tot = 0
for c in range(1, num, 1):
    if num % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')

# concluido