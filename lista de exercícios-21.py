#21. Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva
#a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.
homem1 = int(input("informe a idade de um homem: "))
mulher1 = int(input("informe a idade de uma mulher: "))
homem2 = int(input("informe a idade de outro homem: "))
mulher2 = int(input("informe a idade de outra mulher: "))

if homem1 != homem2:

    if homem1 > homem2 :
        nv = homem2
        vlo = homem1
    elif homem2 > homem1:
        nv = homem1
        vlo = homem2


if mulher1 != mulher2:
    if mulher1 > mulher2 :
        nva = mulher2
        vla = mulher1
        
    elif mulher2 > mulher1:
        nva = mulher1
        vla = mulher2

    
soma = vlo + nva
prod = nv * vla
print(f"a soma é {soma} e o produto é {prod}")


    
    
  



    