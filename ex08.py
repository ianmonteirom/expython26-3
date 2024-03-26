"""
8. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, 
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três 
notas mencionadas anteriormente obedece aos pesos: 
● Trabalho de Laboratório: 2; 
● Avaliação Semestral: 3;
● Exame Final: 5. 
De acordo com o resultado, mostre na tela se o aluno está reprovado (média menor que 4,0), de recuperação 
(igual ou maior que 4 e menor que 6) ou se foi aprovado (igual ou acima de 6).
"""

trab_lab = float(input('Nota do trabalho de laboratório: '))
aval_sem = float(input('Nota da avaliação semestral: '))
exam_final = float(input('Nota do exame final: '))

condic = ''
media = 0

if 0 <= trab_lab <= 10 and 0 <= aval_sem <= 10 and 0 <= exam_final <= 10:
    media = (2 * trab_lab + 3 * aval_sem + 5 * exam_final) / (2 + 3 + 5)
    if media < 4:
        condic = 'REPROVADO'
    elif 4 <= media < 6:
        condic = 'DE RECUPERAÇÃO'
    else:
        condic = 'APROVADO'

print(f'Com a média {media:.2f}, o aluno está {condic}.')
