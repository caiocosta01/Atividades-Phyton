#36. A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um algoritmo que calcule e exiba o salário de um professor. Sabe-se que o valor da hora/aula segue a
#tabela abaixo:
#• Professor Nível 1 R$12,00 por hora/aula
#• Professor Nível 2 R$17,00 por hora/aula
#• Professor Nível 3 R$25,00 por hora/aula

hora = int(input("informe quantas aulas você dá por mês: "))
niv = int(input("informe seu nível de professor: "))

if niv > 3 or niv < 1:
    print("nível inválido, tente novamente!")
    
elif niv == 1:
    salario = 12 * hora
    print(f"este professor receberá R$ {salario} ")
elif niv == 2:
    salario = 17 * hora
    print(f"este professor receberá R$ {salario} ")
elif niv == 3:
    salario = 25 * hora
    print(f"este professor receberá R$ {salario} ")
