peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt**2)

if imc < 18.5:
    print('Baixo peso')
elif imc >= 18.6 and imc < 24.9:
    print('Peso normal')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc < 34.9:
    print('Obesidade grau 1')
elif imc >= 35 and imc < 39.9:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')