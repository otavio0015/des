from random import randint
from time import sleep
print('-' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('-' * 40)
quantos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f' SORTEANDO {quantos} JOGOS '.center(40, '='))
for lista in range(1, quantos + 1):
    sleep(1)
    print(f'Jogo {lista}: {randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60),randint(0, 60), randint(0, 60)}')
print(' < BOA SORTE! > '.center(40, '='))

# concluido