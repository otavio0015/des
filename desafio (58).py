#melhore o jogo do desafio 28 onde o computador vai "pessar" em um numero entre 0 a 10. só que agora o jogador vai tentar advinhar até acertar, mostrado no final quantos palpites foram nescessario para vencer.
from random import randint
sorteio = randint(0, 10)
acertou = False
palpite = 0

print('Vou pensar em um numero entre 0 e 10, tente adivinhar!')
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    if jogador == sorteio:
        acertou = True
    else:
        if jogador > sorteio:
            print('O numero é menor, tente novamente')
        elif jogador < sorteio:
            print('O numero é maior, tente novamente')
    palpite += 1
print(f'Acertou com {palpite} palpites, parabens!')

# concluido