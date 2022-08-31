#47. Modifique a função calculadora() do exercício anterior e faça ela retornar também o resultado da multiplicação e divisão dos parâmetros.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
def calculadora(n1, n2):
    mult = n1*n2
    if n1>n2:
        div = n1/n2
    if n2>n1:
        div = n2/n1
    if n1==n2:
        div = n1/n2
    print(f"a multiplicação dos números é: {mult} e a divisão é: {round(div,2)}")
    return mult, round(div,2)

print(f"{calculadora(n1, n2)}")