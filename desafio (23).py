#faça um progama que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: digite um numero:1834 unidade:4 dezenas:3 centenas:8 e milhar:1
numero = int(input('Digite um numero de quarto digitos: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#concluido