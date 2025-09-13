#faça um progama que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lido.
lista = []
for pessoa in range(5):
    lista.append((float(input(f'Qual o {pessoa + 1}º peso? '))))
maximo = max(lista)
minimo = min(lista)

print(f'O maior peso obitido foi {maximo:.1f}KG\nO menor peso obtido foi {minimo:.1f}KG')

# concluido
