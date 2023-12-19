soma = 0
for n in range(1,101):
    if n % 2 == 0:
        soma = soma + n
print(soma)

soma = 0
for n in range(1, 5):
    nota = float(input('Digite a nota: '))
    if nota <= 10:
        soma = nota 
print(soma) 