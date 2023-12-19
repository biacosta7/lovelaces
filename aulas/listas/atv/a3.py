'''Você está desenvolvendo um programa para uma biblioteca local. O programa deve permitir que os usuários cadastrem livros, fornecendo informações como título, 
autor e 
ano de publicação. 

Implemente um programa em Python que permita o 
cadastro de 3 livros 
imprima o título e o ano de publicação do livro mais antigo.'''


livros = []
anos = []

print("Biblioteca Local\n")

for i in range(3):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação do livro: "))
    livros += [(titulo, autor, ano)]

for livro in livros:
    for i in livro:
        if i == livro[2]:
            anos.append(i)

print(f'\nLivro mais antigo: "{titulo}", {min(anos)}')





'''
for i_ano in livro:
    if i_ano == livro[2]:
        if i_ano 
    


livro = [titulo, ano_atual]
#lista_anos += ano_atual
#livros += [livro]

for ano in lista_anos: 
    if int(ano_atual) > int(ano):
        maior_ano = ano_atual '''

'''
for i in range(3):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_atual = input("Digite o ano de publicação do livro: ")

    livro = [titulo, ano_atual]
    #lista_anos += ano_atual
    #livros += [livro]

    for ano in lista_anos: 
        if int(ano_atual) > int(ano):
            maior_ano = ano_atual 

print(maior_ano)
'''
#funcionando até agora - tenta printar as infos do livro puxando pelo index
#nome_do_vetor.append(novo_valor)

#Adicionar um valor em um índice específico:
#nome_do_vetor.insert(índice, valor)
