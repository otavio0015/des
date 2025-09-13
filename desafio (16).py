#crie um progama que leia um numero real quaquer pelo teclado e mostre na tela a sua porção inteira. ex: 6.127, o numero 6.127 tem a parte inteira 6.
from math import trunc
numero = float (input('digite um numero: '))
print('o numero {} tem a parte inteira {}'.format(numero, trunc(numero)))
#concluido