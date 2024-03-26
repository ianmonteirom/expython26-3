"""
4. Escreva um programa que solicite um número inteiro maior do que zero e menor do que 1000 e exiba a soma
de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido
não for maior do que zero ou menor do que 1000, o programa terminará com a mensagem “Número inválido”.
"""

n = int(input('Digite um número inteiro entre 1 a 999: '))

if 0 < n < 1000:
    n = str(n)
    valores = [int(n[0]), int(n[1]), int(n[2])]
    soma = valores[0] + valores[1] + valores[2]
    print(f'Valor: {soma} ({n[0]} + {n[1]} + {n[2]})')

else:
    print('Número inválido')
