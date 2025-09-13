#Elabore um progamaque calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: Á vista dinheiro/cheque: 10% de desconto, Á vista no cartão: 5% de desconto, em até 2x no cartão : preço normal, e 3x ou mais no cartão: 20% de juros.
preco = float(input('Digite o valor do produto: R$'))

print('''[ 1 ] Á vista dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

pagamento = int(input('Qual a forma de pagamento: '))

if pagamento == 1:
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco, preco - (preco * 10 / 100)))
elif pagamento == 2:
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco, preco - (preco * 5 / 100)))
elif pagamento == 3:
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco, preco))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} Com juros'.format(parcela, (preco + preco * 20 / 100) / parcela))
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco, preco + (preco * 20 / 100)))
else:
    print('Opção invalida.')

#concluido