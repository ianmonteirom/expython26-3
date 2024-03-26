"""
15. Solicite a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições
para aposentadoria são:
Ter pelo menos 65 anos,
Ou ter trabalhado pelo menos 30 anos,
Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

idade = int(input('Idade do trabalhador: '))
tempo = int(input('Tempo de serviço do trabalhador em anos: '))

aposentadoria = False

if idade >= 65:
    aposentadoria = True
if tempo >= 30:
    aposentadoria = True
if idade >= 60 and tempo >= 25:
    aposentadoria = True

if aposentadoria:
    print('O trabalhador pode se aposentar.')
else:
    print('O trabalhador não pode se aposentar.')
