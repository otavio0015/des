#crie um progama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar, considere uss1.00=rs3.27
reais = float (input('digite quanto vc tem em reais: R$ '))
total = (reais / 5.63)

print('seus R$ {} reais valem US$ {:.2f} dolares'.format(reais, total))
#concluido