#39.Dado o nome de um estudante, com o respectivo número de matrícula e as três notas acima mencionadas, desenvolva um algoritmo para calcular a nota final e a classificação de cada estudante. A classificação é dada
#conforme a tabela abaixo:
#Imprima o nome do estudante, com o seu número, nota final e classificação.
nome = str(input("informe seu nome: "))
num = input("informe seu número de matrícula: ")
lab = float(input("informe sua nota no laboratório: "))
lab = lab*2
aval = float(input("informe sua nota na avaliação semestral: "))
aval = aval*3
exam = float(input("informe sua nota no exame final: "))
exam = exam*5

media = (lab+aval+exam)/3

if media >= 10:
    print(f"o aluno {nome} de matrícula n° {num} é classificado como: A com sua pontuação final de: {round(media,2)}" )
if media > 8 and media < 9:
    print(f"o aluno {nome} de matrícula n° {num} é classificado como: B com sua pontuação final de: {round(media,2)}" )
if media > 6 and media < 7:
    print(f"o aluno {nome} de matrícula n° {num} é classificado como: C com sua pontuação final de: {round(media,2)}" )
if media > 4 and media < 5:
    print(f"o aluno {nome} de matrícula n° {num} é classificado como: D com sua pontuação final de: {round(media,2)}" )
if media > 0 and media < 3:
    print(f"o aluno {nome} de matrícula n° {num} é classificado como: R com sua pontuação final de: {round(media,2)}" )