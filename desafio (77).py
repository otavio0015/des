palavras = 'carro', 'peixe', 'bicicleta', 'onibus', 'luz', 'teclado', 'animal', 'leite', 'amendoim'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra, end=' ')

# concluido
