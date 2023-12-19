'''Desenvolva um código que peça ao usuário as medidas de
uma trapézio (base maior, base menor e altura) e uma
função faça uma função que calcule sua área com base na
seguinte fórmula:'''

B = float(input("Base maior: "))
b = float(input("Base menor: "))
h = float(input("Altura: "))

def areaTrapezio(B, b, h):
    area = ((B + b)* h)/2
    return area

print(f'\nÁrea do trapézio = {areaTrapezio(B, b, h)}')