#3. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

dist = float(input("informe a distância total percorrida pelo automóvel: "))
comb = float(input("informe a quantidade de combustível gasta pelo automóvel: "))
cons = dist/comb
print(f"o consumo médio deste automóvel é: {round(cons,2)}")