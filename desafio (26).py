#faça um progama que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A". em que posição ela aparece a primeira vez. em que posição ela aparece a ultima vez.
nome = str(input('Digite seu nome completo: ')).upper().strip()
print('A letra A aparece {} vezes'.format(nome.count('A')))
print('A primeira letra A aparece na posição {}'.format(nome.find('A') + 1))
print('A ultima letra A aparece na posição {}'.format(nome.rfind('A') + 1))
#concluido