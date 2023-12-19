'''
Um furto de celular aconteceu na cidade do RJ e, você foi contratado para desenvolver um programa que possa ajudar sua professora a identificar uma das pessoas envolvidas. Desenvolva uma solução utilizando vetor que faça 5 perguntas para apenas uma pessoa, sendo elas:
“Conhece a vítima do furto?” 
“ Esteve no local do furto?” 
“Mora perto da vítima?” “A vítima lhe devia?” 
“Já trabalhou com a vítima?”
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita” , entre 3 e 4 como “Cúmplice” e 5 como “Ladrão”. Caso contrário, ela será classificada como “Inocente”
'''

lista = ["Conhece a vítima do furto (S/N)? ", 
"Esteve no local do furto (S/N)? ", 
"Mora perto da vítima (S/N)? ", 
"A vítima lhe devia (S/N)? ", 
"Já trabalhou com a vítima (S/N)? "]


sim = []
nao = []

print("\nIdentificação de envolvidos\n")
for pergunta in lista:
    resposta = input(pergunta)

    if resposta == "N" or resposta == "n":
       nao.append(resposta)
    elif resposta == "S" or resposta == "s":
       sim.append(resposta)
    else:
       print("Resposta inválida. Digite S ou N")
       resposta = input(pergunta)

if len(sim) == 2:
   print("\nSuspeita")
elif len(sim) >= 3 and len(sim) <=4:
   print("\nCúmplice")
elif len(sim) == 5:
   print("\nLadrão")
else:
   print("\nInocente")
