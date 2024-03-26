"""
7. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem
peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 6.0.
"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: ')) * 2

media = (n1 * 1 + n2 * 1 + n3 * 2) / (1 + 1 + 2)

print('-'*24)
if media >= 6:
    print(f'Média {media}\n'
          f'Aprovado')
else:
    print(f'Média {media}\n'
          f'Reprovado')
print('-'*24)

