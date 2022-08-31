#37. Faça um algoritmo que calcule o valor da conta de luz de uma pessoa. Sabe-se que o cálculo da conta de luz segue a tabela abaixo:

tipo = input("informe que tipo de construção(residência, comércio ou indústria) deseja calcular a conta de energia: ")
quant = float(input("informe a quantidade de quilowatts por hora consumidos: "))

if tipo == "residência":
    valor = quant * 0.60
    print(f"o valor a ser pago é de R$ {valor}")
if tipo == "comércio":
    valor = quant*0.48
    print(f"o valor a ser pago é de R$ {valor}")
if tipo == "indústria":
    valor = quant*1.29
    print(f"o valor a ser pago é de R$ {valor}")