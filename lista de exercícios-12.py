#12. Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
n1 = float(input("informe o primeiro número: "))
n2 = float(input("informe o segundo número: "))
n3 = float(input("informe o terceiro número: "))

if n1 != n2 and n2 != n3 and n1 != n3:

    if n1 and n2 > n3:
    
        soma = n1+n2
    
        print(f"os maiores valores são {n1} e {n2} e a soma desses valores é {soma}")
    
    elif n3 and n1 > n2:
    
        soma = n1+n3
    
        print(f"os maiores valores são {n1} e {n3} e a soma desses valores é {soma}")
    
    elif n2 and n3 > n1:
    
        soma = n2+n3
    
        print(f"os maiores valores são {n2} e {n3} e a soma desses valores é {soma}")
else:
    print(" os valores são iguais!")
    