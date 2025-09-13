#faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome separadamente. ex: Ana Maria de Souza primeiro = Ana. ultimo = Souza
nome = str(input('Digite o seu nome completo: '))
nome_s = nome.split()
print('Seu primeiro nome é: {}'.format(nome_s[0]))
print('Seu ultimo nome é: {}'.format(nome_s[-1]))
#concluido