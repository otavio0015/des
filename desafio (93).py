jogador = {}
partidas = []
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}: ')))

jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('=' * 60)
print(jogador)
print('=' * 60)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 60)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    -> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')

#concluido
