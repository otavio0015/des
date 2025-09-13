#faça um progama que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo. 
from math import radians, sin, cos, tan
angulo = float(input('digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
#concluido