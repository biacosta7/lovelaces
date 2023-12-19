idade= int(input('Qual a sua idade?: '))


if idade<5:
    print('seu ingresso é gratuito')


elif idade>=5 and idade<12:
     print('seu ingresso é R$10,00')


elif idade>12:
    print('seu ingresso é R$15,00')


else:
    print('seu ingresso é R$7,50')