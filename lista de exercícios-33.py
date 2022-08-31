#33. Faça um algoritmo que receba o nome a idade, o sexo e salário fixo de um funcionário. Mostre o nome e o salário líquido:

nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))
sex = input("informe seu sexo: ")
sf = float(input("informe seu salário fixo: R$ "))
sm = float(input("informe o valor do salário minimo atualmente: "))
if sf < sm:
    if sex == "masculino":
        if idade >= 30:
            sl = sf + 100
        if idade < 30:
            sl = sf + 50
    if sex == "feminino":
        if idade >= 30:
            sl = sf + 200
        if idade < 30:
            sl = sf + 80
    print(f"o funcionário {nome} receberá o salário liquido de R$ {sl} ")
else:
    print("você não está qualificado para o reajuste de salários desta empresa no momento!")