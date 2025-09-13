#desenvolva um progama que leia o nome, idade e sexo de quatro pessoas. no final do progama, mostre: A media de idade do grupo, qual o nome do homen mais velho, quantas mulheres tem menos de 20 anos de idade.
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0

for p in range(4):
    print(f'==== {p + 1}ª pessoa ====')
    nome = str(input(f'Digite o nome: '))
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo [ M ] ou [ F ]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A media da idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomen} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')

# concluido