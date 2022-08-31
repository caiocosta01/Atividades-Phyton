#14. Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).
nome = input("informe o nome do(a) aluno(a): ")
n1 = float(input("informe a primeira nota: "))
n2 = float(input("informe a segunda nota: "))
n3 = float(input("informe a terceira nota: "))
media = (n1+n2+n3)/3
if media >= 7:
    print(f"{nome} foi aprovado(a)!")
elif media <= 5:
    print(f"{nome} foi reprovado(a)!")
elif media > 5.1 and media < 6.9:
    print(f"{nome} está de recuperação!")
    