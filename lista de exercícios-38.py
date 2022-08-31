#38. Faça um algoritmo que leia o nome, o sexo, a altura e a idade de uma pessoa.Calcule e mostre seu nome e o seu peso ideal de acordo com as seguintes características da pessoa. Calcule e mostre nome e o
#seu peso ideal de acordo com as seguintes características da pessoa:

nome = input("informe seu nome: ")
sex = input("informe seu sexo: ")
alt = float(input("informe sua altura: "))
idade = int(input("informe sua idade: "))

if sex == "masculino":
    if alt>1.70:
        if idade<=20:
            peso_ideal = (72.7*alt)-58
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
        if idade>=21 and idade<=39:
            peso_ideal = (72.7*alt)-53
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
        if idade>=40:
            peso_ideal = (72.7*alt)-45
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
    if alt<=1.70:
        if idade<=40:
            peso_ideal = (72.7*alt)-50
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
        if idade>40:
            peso_ideal = (72.7*alt)-58
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
            
if sex == "feminino":
    if alt > 1.50:
        peso_ideal = (62.1*alt)-44.7
        print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
    if alt<=1.50:
        if idade>=35:
            peso_ideal = (62.1*alt)-45
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")
        if idade < 35:
            peso_ideal = (62.1*alt)-49
            print(f"o peso ideal de {nome} é: {round(peso_ideal,2)}")