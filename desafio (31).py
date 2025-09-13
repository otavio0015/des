#desenvolva um progama que pergunte a distancia de uma viagem em km. calcule o preço da passagem. cobrando R$0.50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distancia da sua viagem? '))
curta = distancia * 0.50
longa = distancia * 0.45

if distancia <= 200:
    print('sua viagem é de {}km'.format(distancia))
    print('e o valor é de R${:.2f}'.format(curta))
else:
    print('Sua viagem é de {}km'.format(distancia))
    print('e o valor é de R${:.2f}'.format(longa))

#concluido