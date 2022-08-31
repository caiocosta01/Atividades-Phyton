#11. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
print("informe sua idade")

anos = int(input("em anos: "))
meses = int(input("em meses: "))
dias = int(input("em dias: "))
idade = (anos*365) + (meses*30)+dias
print(f"sua idade em dias é: {idade} dias")


