#16. Faça um programa que receba dois números e execute uma das operações listadas a seguir de acordo com a escolha do usuário. Se for digitada uma opção inválida mostrar mensagem de erro e terminar o programa. As
#opções são:
#• Média entre os dois números.
#• Diferença do maior pelo menor.
#• produto entre os dois números.

n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))

def media1(n1, n2):
    medi = (n1 + n2)/2
    print(f"a media destes dois números é igual a:{medi}")
    
def dif(n1, n2):
    if n1 > n2:
        dif = n1 - n2
        print(f"a diferença entre estes dois números é de:{dif}")
    elif n2 > n1:
        dif = n2-n1
        print(f"a diferença entre estes dois números é de:{dif}")
def prod(n1, n2):
    produ = n1*n2
    print(f"o produto destes dois números é:{produ}")
    
resp = input("informe oque deseja identificar nestes 2 números:(media,diferença ou produto): ")
if resp== "media":
    media1(n1, n2)
elif resp== "diferença":
    dif(n1, n2)
elif resp== "produto":
    prod(n1, n2)
elif resp != "media" and resp != "diferença" and resp != "produto":
    print("opção inválida!")