#27. Faça um algoritmo que leia dois números e identifique se são iguais ou diferentes. Caso eles sejam iguais imprima uma mensagem dizendo que eles são iguais. Caso sejam diferentes,
#informe qual número é o maior, e uma mensagem que são diferentes.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
if n1 == n2:
    print("estes números são iguais!")
if n1 != n2:
    if n1 > n2:
        print(f"eles são diferentes! E o maior número é {n1}")
    elif n2 > n1:
        print(f"eles são diferentes! E o maior número é {n2}")
        