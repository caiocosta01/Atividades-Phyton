#48. Chame a função calculadora() com alguns valores.
def calculadora(n1,n2):
    mult = n1*n2
    if n1>n2:
        div = n1/n2
    if n2>n1:
        div = n2/n1
    if n1==n2:
        div = n1/n2
    soma = n1+n2
    if n1>n2:
        sub = n1 - n2
    if n2>n1:
        sub = n2-n1
    if n1==n2:
        sub = n1-n2
    print(f"a multiplicação dos números é: {mult} a divisão é: {round(div,2)} a subtração é {sub} e a soma é: {soma}")
    return mult, round(div,2), sub, soma

print(f"{calculadora(n1=100,n2=20)}")