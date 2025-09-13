de_maior = homens = mulheres_menor = 0
while True:
    print('=' * 25)
    print('[  Cadastre uma pessoa  ]')
    print('=' * 25)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: '))[0].upper().strip()
        if sexo in 'FM':
            break
        else:
            print('Opção invalida, tente novamente')
            print('Apenas [ F / M ]')
    print('=' * 25)
    while True:
        continua = str(input('Continuar [ S / N] ? '))[0].upper().strip()
        if continua in 'SN':
            break
        else:
            print('Opção invalida, tente novamente')
            print('Apenas [ S / N ]')
    if idade >= 18:
        de_maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1

    if continua == 'N':
        break
print('-=' * 15)
print(sexo)
print(f'Total de pessoas com mais de 18 : {de_maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'e temoas {mulheres_menor} mulheres com menos de 20 anos')

#concluido