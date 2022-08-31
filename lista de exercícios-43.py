#43. Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.
list = []
cntrl = 0

while cntrl < 10:
    list.append(float(input("informe um número: ")))
    cntrl += 1
soma = sum(list)
print(f"a soma dos valores informados é de: {soma} ")