#faca um progama que leia a largura e a altura de uma parede em metros, calcule a sua area e quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
largura = float(input('digite a largura: '))
altura = float(input('digite a altura: '))

total = (altura * largura) / 2

print('a parede é de {}m², voce precisará de {:.2f} litros de tinta'.format(altura * largura, total))
#concluido
