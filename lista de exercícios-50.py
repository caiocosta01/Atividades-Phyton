#50. Fazer uma função que receba como parâmetro um número inteiro e retorne o fatorial desse numero
def fatorial(n):
    fator = 1
    cntr = 1
    while cntr <= n:
        fator = fator*cntr
        cntr += 1
    print(f"o fatorial do número informado é: {fator}")
    return fator

n = int(input("informe um número: "))
fatorial(n)