idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Não pode votar')
elif  idade >= 16 and idade < 18:
    print('Voto opcional')
else:
    print('Voto obrigatório')