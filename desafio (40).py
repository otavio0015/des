#Crie um progama que leia duas notas de um aluno e calcule sua media. mostrando uma mensagem no final, de acordo com a media atingida: Media abaixo de 5.0: reprovado, media entre 5.0 e 6.9: recuperaçao, media 7.0 ous superior: aprovado.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Quem tirou {:.1f} e {:.1f}, a media é de {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Reprovado.')
elif media <= 6.9:
    print('Recuperação.')
else:
    print('Aprovado')

#concluido