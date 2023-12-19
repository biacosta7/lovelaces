'''Crie um programa em Python que solicita ao usuário inserir a quantidade média de horas
de sono por noite. Com base nessa quantidade, o programa deve classificar o usuário em
diferentes estágios de qualidade de sono, considerando os seguintes critérios:
Se a média for menor que 6 horas, exiba "Você pode estar enfrentando uma privação
de sono".
1.

Se a média estiver entre 6 horas (inclusive) e 7 horas (exclusive), exiba "Sua qualidade
de sono é razoável".
2.

Se a média estiver entre 7 horas (inclusive) e 8 horas (exclusive), exiba "Você está
tendo um bom sono".
3.

Se a média for 8 horas ou mais, exiba "Parabéns! Você está tendo um sono
excelente".'''

quantHoras = float(input("Digite quantidade média de horas de sono por noite: "))

if quantHoras < 6:
    print("Você pode estar enfrentando uma privação de sono")
if quantHoras >= 6 and quantHoras < 7:
    print("Sua qualidade de sono é razoável")
if quantHoras >= 7 and quantHoras < 8:
    print("Você está tendo um bom sono")
if quantHoras >= 8:
    print("Parabéns! Você está tendo um sono excelente")