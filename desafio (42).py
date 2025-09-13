#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar qu tipo de triangulo será formado: Equilatero: todos os lados iguais, Isosceles: dois lados iguais e Escaleno: todos os lados diferentes.
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
    
else:
    print('Os segmentos NÃo podem formar triangulo')

#concluido