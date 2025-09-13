#faca um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('digite o preço do produto: R$ '))
desconto = float (preco * 0.05)
total = float (preco - desconto)

print('o produto que custa R$ {} com o desconto de 5%, ele custará R$ {:.2f}'.format(preco, total))
#concluido