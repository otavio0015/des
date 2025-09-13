#faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triagulo retangulo. calcule e mostre o comprimento da hipotenusa
import math
cateto_o = float(input('digite o cateto oposto: '))
cateto_a = float(input('digite o cateto adjacente: '))
hipo = math.hypot(cateto_o, cateto_a)

print('a hipotenusa vai medir {:.2f}'.format(hipo))
#concluido