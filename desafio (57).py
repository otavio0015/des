#faça um progama que leia o sexo de uma pessoa, mas só aceite os valores M ou F. caso esteja errado, peça a digitação novamente até que tenha um valor correto.
sexo = ['F', 'M']
valor = ''

print('Informe seu sexo [ F ] ou [ M ]')
while valor not in sexo:
    valor = str(input('Digite: ')).upper().strip()
    if valor not in sexo:
        print('Dados invalidos, digite apenas [ F ] ou [ V ]')

if valor == 'F':
    print('Sexo Feminino registrado com sucesso')
elif valor == 'M':
    print('Sexo Masculino registrado com sucesso')

#concluido