anoNascimento = int(input("Digite seu ano de nascimento: "))

def calculaIdade(anoNascimento):
    idade = 2023 - anoNascimento
    return idade

def voto(calculaIdade):
    idade = calculaIdade(anoNascimento)
    if idade < 16:
        print("Não vota")
    if idade >= 16 and idade <= 18:
        print("Voto opcional")
    if idade > 18 and idade <= 70:
        print("Voto obrigatório")
    if idade > 70:
        print("Voto opcional")

voto(calculaIdade)