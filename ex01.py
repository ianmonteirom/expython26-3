"""
1. Solicite um número fornecido pelo usuário. Se esse número for positivo, calcule a metade desse número. Se o
número for negativo, mostre o número ao quadrado.
"""

n = float(input('Digite um número: '))
clas = ''
op = ''

if n > 0:
    clas = 'positivo'
    op = 'divido pela metade'
    n = n/2
elif n < 0:
    clas = 'negativo'
    op = 'elevado ao quadrado'
    n = n ** 2

print(f'Seu número é {clas} e {op} resulta em {n}.')
