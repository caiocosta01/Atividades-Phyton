#4. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
nom = input("informe o nome do aluno: ")
n1 = float(input(f"informe a primeira nota do aluno {nom}: "))
n2 = float(input(f"informe a segunda nota do aluno {nom}: "))
n3 = float(input(f"informe a terceira nota do aluno {nom}: "))
media = (n1+n2+n3)/3
print(f"a media adquirida por {nom} é: {media}")