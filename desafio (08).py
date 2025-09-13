#escreva um progama que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('digite o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
km = metros / 1000
hect = metros * 100
decametro = metros * 0.1
decimetro = metros * 10
print('{} centimetros \n{} milimetro \n{} kilometro\n{} hectometro\n{:.2f} decametro\n{} decimetro'.format(centimetros, milimetros, km, hect, decametro, decimetro))
#concluido
