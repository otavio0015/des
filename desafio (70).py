mais1000 = barato = total = menor = cont = barato = 0
print('-=' * 20)
print('         SUPER MERCADO DO TAVÃO')
print('-=' * 20)
print(' ' * 20)
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    print('-=' * 20)
    total += valor
    cont += 1
    
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome

    if valor >= 1000:
        mais1000 += 1
    
    while True:
        continua = str(input('Continuar [ S / N]: '))[0].upper().strip()
        if not continua in 'NS':
            print('Opção invalida, tente novamente')
        elif continua == 'S' or 'N':
            break
    print('-=' * 20)
    if continua == 'N':
        break

print('============ Fim =============')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produto custando mais de R$ 1000.00 reais')
print(f'O produto mais barato que é {barato} custa R${menor:.2f}')
print('-=' * 20)

#concluido
