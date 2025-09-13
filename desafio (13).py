#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('digite seu salario atual: R$ '))
novo = salario + (salario * 15 / 100)

print('seu novo salario é R$ {:.2f}'.format(novo))
#concluido