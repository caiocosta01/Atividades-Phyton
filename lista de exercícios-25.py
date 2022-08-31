#25. Crie um programa onde o usuário informe os valores dos catetos de um triângulo e que ao final mostre a sua hipotenusa.
import math
ca1 = float(input("informe o cateto (a) do triângulo:"))
ca2 = float(input("informe o cateto (b) do triângulo:"))
hip = (ca1**2) + (ca2**2)
hip = math.sqrt(hip)
print(f"a hipotenusa desse triângulo é:{round(hip,2)} cm")
