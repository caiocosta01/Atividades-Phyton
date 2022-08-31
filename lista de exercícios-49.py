#49. Defina uma função divisao() que recebe dois números como parâmetros, calcula e retorna o resultado da divisão do primeiro pelo segundo. Modifique a função velocidade_media()
#utilizando a função divisao() para calcular a velocidade. Teste o seu código chamando a função velocidade_media() com os valores abaixo:
ordem = str(input("oque deseja fazer?(para divisão de dois números, digite: div para calcular a velocidade média digite: vel):"))
if ordem == "div":  
    def divisao(n1, n2):
        div = n1/n2
        print(f"o resultado da divisão dos números é: {div}\n")
        return div
    n1 = float(input("informe o primeiro número: "))
    n2 = float(input("informe o segundo número: "))
    divisao(n1, n2)
if ordem == "vel":
    def velocidade_media(distancia, tempo):
        if distancia<=0:
            print("distãncia informada inválida!")
        elif tempo<=0:
            print("tempo informado inválido!")
        else:
            v = distancia/tempo  
            print(f"a velocidade média deste veiculo foi de: {round(v,2)}")
            return round(v,2)
    n1 = float(input("informe a distãncia total percorrida(em km): "))
    n2 = float(input("informe o tempo total gasto(em horas): "))
    velocidade_media(n1, n2)


    
    
