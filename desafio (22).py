#crie uma progama que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas. o nome com todas minuscula. quantas letras ao todo(sem considerar espaços). quantas letras tem o primeiro nome.
nome = str (input('Digite seu nome: ')).strip()
separa = nome.split()
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} Letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
#concluido
