#34. Escrever um algoritmo que leia três valores inteiros distintos e os escreva em ordem crescente.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
n3 = float(input("informe o terceiro número: "))
if n1<n2 and n2<n3:
    print(f"a ordem crescente dos valores informados é: {n1, n2, n3}")
if n2<n1 and n1<n3:
    print(f"a ordem crescente dos valores informados é: {n2, n1, n3}")
if n3<n1 and n1<n2:
    print(f"a ordem crescente dos valores informados é: {n3, n1, n2}")
if n3<n2 and n2<n1:
    print(f"a ordem crescente dos valores informados é: {n3, n2, n1}")
if n1<n3 and n3<n2:
    print(f"a ordem crescente dos valores informados é: {n1, n3, n2}")
if n2<n3 and n3<n1:
    print(f"a ordem crescente dos valores informados é: {n2, n3, n1}")
