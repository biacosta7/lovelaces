'''
Crie um programa em Python para ajudar uma pequena
empresa a registrar informações sobre seus
funcionários. A empresa tem 10 funcionários e deseja
saber 
quantos deles são do sexo feminino, 
quantos são do sexo masculino e 
qual é a média de idade de todos os funcionários. 

Ou seja peça ao usuário seu
nome, sexo e idade.

Se o funcionário for do sexo feminino deve digitar “F”

Se o funcionário for do sexo masculino deve digitar “M”

'''
mulheres = 0
homens = 0
idades = 0

for i in range(1, 11):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    
    sexo = input('Digite F (feminino) ou M (masculino): ').upper()
    
    if sexo == 'F':
        mulheres += 1
    elif sexo == 'M':
        homens += 1
    else:
        print('Inválido')
    
    idades += idade
    media_idades = idades/10

print()
print('Existem', mulheres, 'funcionários do sexo feminino.')
print('Existem', homens, 'funcionários do sexo masculino.')
print('A média das idades dos funcionários é igual a', media_idades)