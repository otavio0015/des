#crie um progama que leia a data de nascimento de sete pessoas. no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(7):
    nasc = int(input(f'Em que ano a {pessoa + 1}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')

# concluido
