valor = int(float(input()) * 100)
notas = (10000, 5000, 2000, 1000, 500, 200)
moedas = (100, 50, 25, 10, 5, 1)

print('NOTAS:')
for v in range(len(notas)):
    nota = valor // notas[v]
    valor = valor % notas[v]
    print(f'{nota} nota(s) de R$ {notas[v] / 100:.2f}')

print('MOEDAS:')
if valor >= 0:
    for m in range(len(moedas)):
        moeda = valor // moedas[m]
        valor = valor % moedas[m]
        print(f'{moeda} moeda(s) de R$ {moedas[m] / 100:.2f}')