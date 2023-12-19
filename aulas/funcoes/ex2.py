def media(nota1, nota2, nota3):
    med = (nota1 + nota2 + nota3)/3
    return med


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
m = media(nota1, nota2, nota3)
print("\nMÉDIA: ", m)

def estado(m):
    if m >= 7:
        return "Aprovado"
    elif m < 7 and m > 4:
        return "Recuperação"
    else:
        return "Reprovado"

print(estado(m))