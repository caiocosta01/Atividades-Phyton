#40. Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir
#apólices de seguro. Quanto às classes de ocupações, foram definidos três grupos de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco. Dados nome,
#idade e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a categoria do pretendente, e, caso a idade não esteja na faixa
#necessária, imprimir uma mensagem.
nome = str(input("informe seu nome: "))
idade = int(input("informe sua idade: "))
grupo_risco = str(input("informe o nível do seu grupo de risco (baixo, médio e alto): "))

if idade>=17 and idade<=20:
    if grupo_risco == "baixo":
        print(f"{nome} com {idade} anos é de categoria 1 !")
    if grupo_risco == "médio":
        print(f"{nome} com {idade} anos é de categoria 2 !")
    if grupo_risco == "alto":
        print(f"{nome} com {idade} anos é de categoria 3 !")
elif idade >=21 and idade<=24:
    if grupo_risco == "baixo":
        print(f"{nome} com {idade} anos é de categoria 2 !")
    if grupo_risco == "médio":
        print(f"{nome} com {idade} anos é de categoria 3 !")
    if grupo_risco == "alto":
        print(f"{nome} com {idade} anos é de categoria 4 !")
elif idade >=25 and idade<=34:
    if grupo_risco == "baixo":
        print(f"{nome} com {idade} anos é de categoria 3 !")
    if grupo_risco == "médio":
        print(f"{nome} com {idade} anos é de categoria 4 !")
    if grupo_risco == "alto":
        print(f"{nome} com {idade} anos é de categoria 5 !")
elif idade >=35 and idade<=64:
    if grupo_risco == "baixo":
        print(f"{nome} com {idade} anos é de categoria 4 !")
    if grupo_risco == "médio":
        print(f"{nome} com {idade} anos é de categoria 5 !")
    if grupo_risco == "alto":
        print(f"{nome} com {idade} anos é de categoria 6 !")
elif idade >= 65 and idade <= 70:
    if grupo_risco == "baixo":
        print(f"{nome} com {idade} anos é de categoria 7 !")
    if grupo_risco == "médio":
        print(f"{nome} com {idade} anos é de categoria 8 !")
    if grupo_risco == "alto":
        print(f"{nome} com {idade} anos é de categoria 9 !")
else:
    print("nã se encontram disponíveis apólices de seguro de acordo com a idade informada!")