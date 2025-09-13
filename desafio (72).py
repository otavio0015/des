while True:
    numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quize', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
    escolha = int(input('Digite um numero de 0 a 20: '))
    if escolha <= 20:
        print(f'voce escolheu o numero {numeros[escolha]}')
        break
    else:
        print('Tente novamente!')

# concluido