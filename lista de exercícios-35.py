#35. Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os lados de um triângulo. Se forem informar qual o tipo de triângulo que eles formam:
#equilátero,isóscele ou escaleno. Propriedade: o comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.
n1 = int(input("informe o primeiro número: "))
n2 = int(input("informe o segundo número: "))
n3 = int(input("informe o terceiro número: "))
if n1 < n2+n3 and n2<n1+n3 and n3<n1+n2:
    if n1==n2==n3:
        print("Triângulo Equilátero")
    elif n1==n2 or n2==n3 or n1==n3:
        print("Triâgulo Isócele")
    elif n1 != n2 or n2 != n3 or n1!=n3:
        print("Triângulo Escaleno")
else:
    print("os números informados não podem ser os lados de um triângulo!")