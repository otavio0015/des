from random import randint
funcao = ''
tentativa = 0
while True:
    computador = randint(0, 10)
    print('-=' * 25)
    numero = int(input('Digite um numero: '))
    while True:
        jogador = str(input('Digite sua opção [ P / I]: '))[0].strip().upper()
        if jogador in 'IP':
            break
        else:
            print('opção invalida, tente novamente')

    print('-=' * 25)
    total = computador + numero

    if total %2 == 0:
        funcao = 'P'
        print('Deu PAR')
    else:
        funcao = 'I'
        print('Deu IMPAR')

    if funcao == jogador:
        print('Você ganhou')
        tentativa += 1
    else:
        print('Você perdeu')
        break
print(f'Computador escolheu {computador} e você {numero}, total de {computador + numero}')
print(f'Vitorias = {tentativa}')
print('-=' * 25)

#concluido