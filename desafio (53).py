#crie um progama que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite o nome: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if inverso == junto:
    print(f'O inverso de [ {junto} ] é [ {inverso} ]\nEntão ele é um palíndromo')
else:
    print(f'O inverso de [ {junto} ] é [ {inverso} ]\nEntão ele NÃO é um palíndromo')

# concluido