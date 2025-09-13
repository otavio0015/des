#escreva um progama que leia a velocidade de um carro. se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
velocidade = float(input('Digite a velocidade do carro: '))
limite = 80
multa = (velocidade - limite) * 7

if velocidade > limite:
    print('{}km/h Você foi multado será de R${:.2f}'.format(velocidade, multa))
    print('a velocidade permitida é 80km/h')
else:
    print('Você está na velocidade permitida')

#concluido