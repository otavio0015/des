#Desenvolva um progama que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.
import math
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Não é possivel fazer um triangulo')
else:
    print('esse comprimentos dá para fazer um triangulo')

#concluido