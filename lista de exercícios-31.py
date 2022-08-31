#31. Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
#• Ter no mínimo 65 anos de idade.
#• Ter trabalhado no mínimo 30 anos.
#• Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
idade = int(input("informe sua idade: "))
anos = int(input("informe quantos anos você trabalhou: "))
if idade >= 65:
    print("você está qualificado para a aposentadoria!")
if anos > 30:
     print("você está qualificado para a aposentadoria!")
if idade > 60 and anos > 25:
    print("você está qualificado para a aposentadoria!")
else:
    print("você não está qualificado para a aposentadoria!") 