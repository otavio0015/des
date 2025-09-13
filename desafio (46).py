#faca um progama que mostre na tela contagem regressiva para o estouro dos fogos de artificio. indo de 10 até 0. com a pausa de 1 segundo entre elas.
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('🎆')

#concluido