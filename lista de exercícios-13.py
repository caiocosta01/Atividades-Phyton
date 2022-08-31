#13. Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

n1 = float(input("informe um número: "))
if n1 > 100 and n1 < 200:
    print("o número informado está no intervalo entre 100 e 200")
else:
    print("o número não faz parte do intervalo entre 100 e 200")