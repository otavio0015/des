galera = []
pessoa = {}
mulher = 0
cont = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    cont += 1
    while True:
        pessoa['sexo'] = str(input('Sexo [M / F]: ')).upper()[0]
        if pessoa['sexo'] == 'F':
            mulher += 1
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, Por favor digite apenas M ou F.')


    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar [S / N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')

    if resp == 'N':
        break

soma_idades = sum([pessoa['idade'] for pessoa in galera] / cont)

print('-=' * 30)
print(galera)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {soma_idades:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulher}')

