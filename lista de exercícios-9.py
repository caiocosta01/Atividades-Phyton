#9. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior.
n1 = int(input("informe o primeiro número: "))
n2 = int(input("informe o segundo número: "))
if n1 > n2:
    print(f"o número {n1} é o maior")
if n2 > n1:
     print(f"o número {n2} é o maior")
if n1==n2:
    print(" estes números são iguais!")