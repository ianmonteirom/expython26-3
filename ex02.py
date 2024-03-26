"""
2. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença
existente entre ambos.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
maior = 0
diff = 0

if n1 > n2:
    maior = n1
    diff = n1 - n2
elif n2 > n1:
    maior = n2
    diff = n2 - n1

print(f'O maior número entre os dois é {maior}. A diferença existente entre ambos é de {diff}.')
