#46. Agora faça uma função calculadora() que recebe dois números como parâmetros e retorna o resultado da soma e da subtração entre eles.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
def calculadora(n1, n2):
    soma = n1+n2
    if n1>n2:
        sub = n1 - n2
    if n2>n1:
        sub = n2-n1
    if n1==n2:
        sub = n1-n2
    print(f"a soma dos números é: {soma} e a subtração é: {sub}")
    return soma, sub

print(f"{calculadora(n1, n2)}")