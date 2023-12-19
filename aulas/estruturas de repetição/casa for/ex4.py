'''
Crie um programa que receba 4 notas de um aluno.
E em seguida imprima sua media geral e se o aluno
foi aprovado ou reprovado.

Para o aluno ser aprovado ele precisa tirar média
maior ou igual a 7.

Para o aluno ser reprovado ele precisa tirar
média menor que 7.
'''

list = 0
for i in range(4):
    nota = float(input('Digite a nota: '))
    if nota <= 10:
        list += nota
media = list/4

if media >= 7:
    print()
    print('Você foi aprovado.')
else:
    print()
    print('Você foi reprovado.')

print('Sua média:', media)
