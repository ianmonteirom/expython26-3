"""
13. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo. Considere o seguinte
conceito: O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
"""

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')
