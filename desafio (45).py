#Crie um progama que faça o computador jogar Jokenpô com você.
from random import choice

print('Vamos jogar Pedra, Papel e Tesoura')
computador = ['pedra', 'papel', 'tesoura']
jogador = str(input('Escolha Pedra, Papel ou Tesoura: ')).lower()
sorteio = choice(computador)

if jogador == sorteio:
    print(f'empate, eu tambem escolhi {sorteio}')
elif (jogador == 'pedra' and sorteio == 'tesoura') or (jogador == 'papel' and sorteio == 'pedra') or (jogador == 'tesoura' and sorteio == 'papel'):
    print(f'vc ganhou, eu escolhi {sorteio}')
else:
    print(f'Vc perdeu, eu escolhi {sorteio}')

#concluido