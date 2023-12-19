lista =["Beatriz", "Laura", "Luísa", "Julia", "Mariana"]

convidada = input("Nome da convidada: ")

for i in lista:
    if convidada == i:
        print("Está na lista")
else:
    print("Não está na lista")