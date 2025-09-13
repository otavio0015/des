km = float(input('qual a distacia pecorida em km: '))
dia = int(input('quantos dias ele foi alugado: '))
total = (dia * 60) + (km * 0.15)

print('o total a pagar é de R${:.2f}'.format(total))
#concluido