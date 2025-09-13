#A confederação nacional de natação precisa de um progama que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: mirim, Até 14 anos: infantil, Até 19 anos: Junior, Até 25 anos:senior e acima: Master
from datetime import date
data = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = data - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificação: Mirim')
elif idade <= 14:
    print('classificação: Infantil')
elif idade <= 19:
    print('classificação: Junior')
elif idade <= 25:
    print('classificação: Senior')
else:
    print('classificação: Master')

#concluido