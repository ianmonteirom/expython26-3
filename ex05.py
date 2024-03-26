"""
5. Chama-se de capicua qualquer número que, quando lido da esquerda para a direita é o mesmo que quando lido
da direita para a esquerda. São exemplos de capicua, por exemplo, os números 212, 303, 848. Faça um algoritmo
para ler um número inteiro com três algarismos e exiba uma mensagem informando se esse número é capicua
ou se não é capicua.
"""

num = int(input('Digite um número com três algorismos: '))
numstr = str(num)

frente = [numstr[0], numstr[1], numstr[2]]
tras = [numstr[2], numstr[1], numstr[0]]

if frente == tras:
    print(f'O número {num} é capicua.')
else:
    print(f'O número {num} não é capicua.')
