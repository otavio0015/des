#dessenvolva um progama que leia o primeiro termo e a razão de PA. no final mostre os dez primeiros termos dessa progressão.
print('=' * 30)
print(' ' * 5, '10 TERMOS DE UMA PA', ' ' * 5)
print('=' * 30)

pritermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pritermo + (10 - 1) * razao
for num2 in range (pritermo, decimo + razao, razao):
    print(num2, end=' -> ')
print('ACABOU')

# concluido