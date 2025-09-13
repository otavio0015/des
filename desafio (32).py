#faça um progama que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite um ano qualquer: '))
bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if ano - ano == bissexto:
    print('O ano de {} não é bissexto'.format(ano))
else:
    print('O ano de {} é bissexto'.format(ano))

#concluido