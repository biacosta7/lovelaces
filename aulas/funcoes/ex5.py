'''Crie uma função chamada conta_vogais que recebe uma string como
argumento e retorna o número de vogais na string. Considere que as
vogais ‘a’
,
‘e’
,
‘i’
,
‘o’ e ‘u’

, independentemente de serem maiúsculas ou

minúsculas

Em seguida, crie um programa principal que solicita ao usuário que
insira uma palavra ou frase e utiliza a função ‘conta_vogais‘ para contar
e exibir o número de vogais na entrada.'''



texto = input("Insira palavra ou frase: ").lower()

def conta_vogais(texto):
    numeroVogais = 0
    vogais = ["a", "e", "i", "o", "u"]

    for letra in texto:
        if letra in vogais:
            numeroVogais += 1
    return numeroVogais

print(f"Número de vogais: {conta_vogais(texto)}")


