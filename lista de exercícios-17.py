#17. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se sa
#ldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

num_conta = input("informe o numero da sua conta: ")
saldo = float(input("informe seu saldo em conta:R$ "))
debit = float(input("informe seu débito :R$ "))
credit = float(input("informe seu crédito em conta:R$ "))
saldo_atual = (saldo - debit)+ credit
if saldo_atual >= 0:
    print(f"seu saldo atual é de: R$ {saldo_atual} saldo positivo")
else:
    print(f"seu saldo atual da conta '{num_conta}' é de: R$ {saldo_atual} saldo negativo")