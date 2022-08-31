#23. Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe média de preço
#de custo e do preço de venda.
cntrl = 0
list = []
list2 =[]
while cntrl < 40:
    preco_custo = float(input("informe o preço de custo do produto: R$ "))
    list.append(preco_custo)
    media = preco_custo + preco_custo
  
    preco_venda = float(input("informe o preço de venda do produto: R$ "))
    list2.append(preco_venda)
    
    media2 = preco_venda + preco_venda
    if preco_custo < preco_venda:
        print("houve lucro!")
    elif preco_venda < preco_custo:
         print("houve prejuízo!")
    elif preco_venda == preco_custo:
        print("empate de preço!")
    cntrl += 1
soma = sum(list)
soma2 = sum(list2)
print(f"a média de preço de custo é de: R$ {soma/40}")
print(f"a média de preço de venda é de: R$ {soma2/40}")