"""
3. Faça um programa que solicite 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média
destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0. Caso a nota não possua
um valor válido, este fato deve ser informado ao usuário e o programa finalizado.
"""

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    media = (n1 + n2) / 2
    print(f'Média: {media}')
else:
    print('Erro! Verifique os valores informados e tente novamente.')
