#Faça um progama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda se alistar ao serviço militar. se é a hora de se alistar. se já passou do tempo do alistamento. seu progama tambem deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Qual ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alista imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não tem 18 anos, falta {} anos'.format(saldo))
    print('Seu alistamento será em {}'.format())
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

#concluido