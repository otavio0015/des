#crie um progama que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('a sua cidade tem o nome Santo: {}'.format(cidade[:5].upper() == 'SANTO'))
