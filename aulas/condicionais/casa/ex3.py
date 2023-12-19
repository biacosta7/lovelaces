admissao = int(input('Digite o ano de admissão: '))
sal = float(input('Digite o valor do seu salário: '))
reajuste = int(input('Digite o ano do último reajuste salarial: '))
anos = reajuste - admissao  

if anos > 10:
    x = (sal * (30/100)) + sal
    print('Você receberá R$', x)

elif anos >= 5 and anos <= 10:
    x = (sal * (20/100)) + sal
    print('Você receberá R$', x)

elif anos < 5 and anos >= 2:
    x = (sal * (10/100)) + sal
    print('Você receberá R$', x)
    
else:
    print('Você não está apto ao reajuste salarial coletivo.')
