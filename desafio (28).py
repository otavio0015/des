#escreva um progama que faça o computador "pensar" em um numero entre 0 e 5 e peça para o usuario tentar descobrie qual foi o numero escolhido pelo computador. o progama deverá escrever na tela se o usuario venceu ou perdeu.
from time import sleep
from random import randint
numero = int(input('Tente adivinhar um numero de 0 a 5 que eu pensei? '))
sorteio = randint(0, 5)
print('PROCESSANDO . . .')
sleep(3)
if numero == sorteio:
    print('vc acertou, eu pensei no numero {}'.format(sorteio))
else:
    print('vc errou, eu pensei no numero {}'.format(sorteio))

#concluido