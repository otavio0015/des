#escreva um progama que pergunte o sálario de um funcionario e calcule o valor do seu aumento. para salarios superiores a R$1.250,00, calcule um aumento de 10%. para os inferiores ou iguais. o aumento é de 15%
salario = float(input('Qual o seu salario atual? R$'))
superior = salario * 0.10 + salario
inferior = salario * 0.15 + salario
if salario > 1250:
    print('\033[0;32;40m O salario de R${:.2f} com aumento de 10%, ficará R${:.2f}'.format(salario, superior))
else:
    print('O salario de R${:.2f} com aumento de 15%, ficará R${:.2f}'.format(salario, inferior))

#concluido