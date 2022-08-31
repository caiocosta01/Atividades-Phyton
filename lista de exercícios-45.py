#45. Defina uma função soma() que recebe dois números como parâmetros e calcula a soma entre eles.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
def soma(n1,n2):
    s = n1+n2
    print(f"a soma dos dois valores é: {s}")
soma(n1, n2)