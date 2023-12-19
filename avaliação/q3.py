''''
Faça um programa para uma sorveteria que solicite ao usuário um sabor de sorvete, dentre os 3 existentes: Chocolate, Morango e Flocos:
Caso o usuário digite Chocolate, exiba na tela “o valor do sorvete é R$3.00”;
Caso o usuário digite Morango, exiba na tela “o valor do sorvete é R$4.00”; 
Caso o usuário digite Flocos, exiba na tela “o valor do sorvete é R$5.00”.
Para qualquer outro sabor de sorvete, deve ser exibido na tela “o valor do seu sorvete é R$6.00”
'''
sabor = input('Escolha o sabor do sorvete (chocolate, morango ou flocos): ')

if sabor == 'chocolate':
    print('O valor do sorvete é R$3.00')
elif sabor == 'morango':
    print('O valor do sorvete é R$4.00')
elif sabor == 'flocos':
    print('O valor do sorvete é R$5.00')
else:
    print('O valor do seu sorvete é R$6.00')