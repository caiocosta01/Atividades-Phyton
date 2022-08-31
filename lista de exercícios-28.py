#28. Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não esteja neste intervalo, exibir mensagens: número inválido.
n = int(input("informe um número entre 1 e 5: "))
if n < 1 or n > 5:
    print("número inválido!")

if n == 1:
    print("um")
if n == 2:
    print("dois")
if n == 3:
    print("três")
if n == 4:
    print("quatro")
if n == 5:
    print("cinco")
