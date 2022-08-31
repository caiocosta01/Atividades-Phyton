#26. Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.
cntrl = "n"
while cntrl != "s":
    n = float(input("informe um número: "))
    if n > 0:
        print("este número é positivo!")
    if n < 0 :
        print("este número é negativo!")
    if n == 0:
        print("este número é igual a zero!")
    cntrl = input("deseja encerrar o programa? s/n ")