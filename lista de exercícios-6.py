#6. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
compra = float(input("informe o valor da compra: "))
mensais = compra/5
print(f"as prestações serão do valor: R${round(mensais,2)}")