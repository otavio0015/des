#Escreva um progama para aprovar o emprestimo bancario para a compra de uma casa. O progama vai perguntar o valor da casa. o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal. Sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
ano = int(input('Quantos anos de finaciamento? '))
prestacao = casa / (ano * 12)
minimo = salario * 30 /100
print('Para pagar um casa de R${:.2f} em {:.2f} anos'.format(casa, ano))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser consedido!')
else:
    print('Emprestimo negado!')

#concluido