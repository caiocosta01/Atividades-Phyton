#30. A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente.
#O desconto deverá ser calculado sobre o valor do veículo de acordo com o combustível (álcool – 25%, gasolina – 21% ou diesel –14%). Com valor do veículo zero encerra entrada de dados.
#Informe total de desconto e total pago pelos clientes.
list1 = list2 = []

valor_veiculo = 1
while(valor_veiculo != 0):
    valor_veiculo = float(input("informe o valor do veículo: R$ "))
    valor_veiculo = valor_veiculo - 1
    combus = input("informe o combustível do veículo escolhido: ")
    
    if(combus == "álcool"):
        valor_desconto = valor_veiculo*0.25
        list1.append(valor_desconto)
        valor_veiculo = valor_veiculo - (valor_veiculo*0.25)
        list2.append(valor_veiculo)
        print(f"na compra deste veículo o cliente ganha R$ {valor_desconto} e o valor do veículo sai por R$ {valor_veiculo} ")
    
    elif(combus == "gasolina"):
        valor_desconto = valor_veiculo*0.21
        list1.append(valor_desconto)
        valor_veiculo = valor_veiculo - (valor_veiculo*0.21)
        list2.append(valor_desconto)
        print(f"na compra deste veículo o cliente ganha R$ {valor_desconto} e o valor do veículo sai por R$ {valor_veiculo}")
    
    elif(combus == "diesel"):
        valor_desconto = valor_veiculo*0.14
        list1.append(valor_desconto)
        valor_veiculo = valor_veiculo - (valor_veiculo*0.14)
        list2.append(valor_desconto)
        print(f"na compra deste veículo o cliente ganha R$ {valor_desconto} e o valor do veículo sai por R$ {valor_veiculo} ")
    else:
        print("combustível inválido!")

desconto = sum(list1)
pago = sum(list2)
print(f"o total de desconto distribuido pela empresa CARANGO é de R$ {desconto} e o valor total pago pelos clientes é de R$ {pago} ")