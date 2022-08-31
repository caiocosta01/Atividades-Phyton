#44. Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números. Depois de ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos
#e a média dos números lidos.
quant = int(input("informe a quantidade de números que este programa deve ler: "))
cntrl = 0
list = []
while cntrl<quant:
    list.append(float(input("informe um número: ")))
    cntrl += 1
maior = max(list)
soma = sum(list)
media = soma/quant
print(f"entre os valores informados, o maior foi: {maior} e a média dos valores informados é {round(media,2)}")

