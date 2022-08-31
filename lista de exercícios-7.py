#7. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo
#usuário.

preco_cus = float(input("informe o preço de custo do produto: R$ "))
porcent = float(input("informe a porcentagem de acréscimo ao preço de custo: "))
porcent2 = porcent/100
preco_venda = (porcent2*preco_cus)+preco_cus
print(f"o preço de venda deste produto é: R$ {preco_venda}")


