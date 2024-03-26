"""
14. Faça um algoritmo que solicite 3 valores a, b, c, onde a, b, c, são quaisquer valores reais. Exibir na tela uma
mensagem informando se os valores estão em: ordem crescente; ordem decrescente; ou desordenado.
"""

a = float(input('Digite o primeiro valor real: '))
b = float(input('Digite o segundo valor real: '))
c = float(input('Digite o terceiro valor real: '))

if a < b < c:
    print('Ordem crescente.')
elif a > b > c:
    print('Ordem decrescente.')
else:
    print('Valores desordenados.')
