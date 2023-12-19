valor = float(input("Digite o valor do produto: "))
cupom = input("Digite o cupom de desconto: ")

if cupom == "DESC10":
    print(f'R${valor - (valor * 10/100)}')

elif cupom == "FRETEGRATIS":
    print(f'R${valor} - Frete grátis incluso')

else:
    print(f'R${valor}')