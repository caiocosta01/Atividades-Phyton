#10. Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
ano_atual = int(input("informe o ano atual: "))
ano_nasc = int(input("informe seu ano de nascimento:"))
if ano_atual - ano_nasc >16:
    print("você poderá votar este ano!")
else:
    print("você não poderá votar este ano!")