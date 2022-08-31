#20. Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. No final informe total de homens e de mulheres.
contro = 0
cont = 0
cont2 = 0
while contro < 56:
    nome = input("informe seu nome: ")
    sexo = input("informe seu sexo: ")
    if sexo == "feminino":
        cont += 1
        print(f"{nome} é uma mulher")
    elif sexo == "masculino":
        cont2 += 1
        print(f"{nome} é um homem")
    contro += 1
print(f"ha {cont} mulheres e {cont2} homens")