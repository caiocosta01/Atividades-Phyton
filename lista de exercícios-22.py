#22. Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.
contro = "n"
contador = 0


while contro != "s":
    nome = input("informe seu nome: ")
    sex = input("informe seu sexo: ")
    idad = int(input("informe sua idade: "))
    saude = input("você está bem de saúde?")
    
    if sex == "masculino" and idad > 18 and saude == "sim":
        contador += 1
        print(f"você está apto para o serviço militar!")
    else:
       print("você não está apto para o serviço militar!")
    contro = input("deseja encerrar o programa?s/n:")
print(f"estão aptas para o alistamento militar:{contador} pessoas!")
    