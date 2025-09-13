listagem = ('feijão', 8.50,
            'arroz', 5.70,
            'macarrão', 5,
            'miojo', 2,
            'bolacha', 5,
            'biscoito', 4,
            'coxa de frango', 13,
            'creme de leite', 4.50)

print('=' * 40)
print(f'{'LISTAGEM DE PREÇO':^40}')
print('=' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 40)

# concluido