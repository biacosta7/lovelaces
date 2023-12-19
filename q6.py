produtos = []
valor = []


for a in range(10):
    p = str(input(f'Digite o nome do {a}° Podruto:'))
    v = float(input(f'Digite o valor do {a}° Podruto:'))
    produtos.append(p)
    valor.append(v)


print('''Sua conta será paga por meio de PIX ou CARTÃO DE CRÉDITO? '
        [1]PIX
        [2]CARTÃO DE CRÉDITO''')
pag = int(input('Digite o número equivalente a função escolhida: '))


soma = 0
for v in valor:
    soma += v
print(f'O valor da sua compra é {soma}')


valor_pagar = 0
if soma > 100:
    if pag == 1:
        desc = (soma * 15/100)
        valor_pagar = soma - desc
        print(f'Você recebeu um desconto de 15%, o valor da sua compra é {valor_pagar}')
elif pag == 1:
    print('Leia o QR code por favor.')
elif pag == 2:
    print(f'Coloque o catão na maquineta')
else:
    print('Erro no sistema')
