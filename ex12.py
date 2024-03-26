"""
12. Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5, mas não
simultaneamente pelos dois.
"""

n = int(input('Digite um número inteiro: '))

if n % 3 == 0 and n % 5 == 0:
    print(f'{n} é divisível simultaneamente pelos dois.')

if n % 3 != 0 or n % 5 != 0:
    if n % 3 == 0:
        print(f'{n} é divisível por 3.')
    if n % 5 == 0:
        print(f'{n} é divisível por 5.')

if n % 3 != 0 and n % 5 != 0:
    print(f'{n} não é divisível por 3 nem por 5.')
