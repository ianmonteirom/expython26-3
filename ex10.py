"""
10. Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (+, -, /, *). O
usuário escolhe uma das opções e o seu programa então pede dois valores numéricos, realiza a operação e
mostra o resultado.
"""

print('1 - Somar (+)\n'
      '2 - Subtrair (-)\n'
      '3 - Dividir (/)\n'
      '4 - Multiplicar (*)')

res = 0
op = ''
escolha = int(input('Escolha uma das opções: '))
if 1 <= escolha <= 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    if escolha == 1:
        res = n1 + n2
        op = '+'
    elif escolha == 2:
        res = n1 - n2
        op = '-'
    elif escolha == 3:
        res = n1 / n2
        op = '/'
    elif escolha == 4:
        res = n1 * n2
        op = '*'
    print(f'{n1} {op} {n2} = {res}')
else:
    print('Erro! Escolha uma opção válida!')
