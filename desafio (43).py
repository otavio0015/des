#Desenvolva um logica que leia o peso e a altura de uma pessoa. calcule seu IMC a mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5: abaixo do peso. Entre 18.5 e 25: peso ideal. 25 até 30: sobrepeso. 30 até 40: obesidade. acima de 40: obesidade mórbida.
altura = int(input('Digite a sua altura em cm: '))
peso = int(input('Digite a seu peso: '))
total = peso / ((altura / 100) ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(total))
if total < 18.5:
    print('Abaixo do peso')
elif total < 25:
    print('Peso ideal')
elif total < 30:
    print('Sobrepeso')
elif total < 40:
    print('Obesidade')
else:
    print('obesidade mórbida')

#concluido