"""
9. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
Lembre-se: a base maior e a base menor devem ser, obrigatoriamente, números maiores que zero.
"""

base_menor = float(input('Digite a base menor do trapézio: '))
base_maior = float(input('Digite a base maior do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

if base_maior > 0 and base_menor > 0:
    area = (base_maior + base_menor) * altura / 2
    print(f'A área do trapézio é de {area}.')
else:
    print('Erro! Verifique os dados e tente novamente! A base maior e a base menor devem ser maiores que zero.')
