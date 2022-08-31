#15. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
compra = int(input("informe a quantidade de maçãs compradas: "))
if compra >= 12:
    cust_tot = compra*1
    print(f"o valor total da compra foi de: R${cust_tot}")
else:
    cust_tot = compra*1.30
    print(f"o valor total da compra foi de: R${cust_tot}")
