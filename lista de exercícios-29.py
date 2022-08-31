#29. Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada
#a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem
#‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.
c_u = 1234
n = 0
se = 9999
n2 = 0
while n != c_u:
    n = int(input("infome seu código de usuário: "))
    if n != c_u:
        print("usuário inválido!")
while n2 != se:
    n2 = int(input("informe sua senha: "))
    if n2 != se:
        print("senha incorreta!")
    if n2 == se:
        print("acesso permitido! Bem vindo! ")
    
    