peso = float(input('Digite o peso do pacote: '))

if peso <= 1:
    print('O custo é de R$10')
elif peso > 1 and peso <= 10:
    print('O custo é de R$30')
elif peso > 10 and peso <= 50:
    print('O custo é de R$60')
else:
    print('O custo é de R$100')