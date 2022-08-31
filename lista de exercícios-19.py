#19. Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e“menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior
#de idade.
contro = 0

while contro < 75:
    idade = int(input("informe sua idade: "))
    if idade >= 18:
        print(f"Maior de idade!")
    else:
        print("Menor de idade!")
    contro += 1