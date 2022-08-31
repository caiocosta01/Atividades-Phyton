#42. Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.
cntl = 0
contador = 0
while cntl < 10:
    n = float(input("informe um número: "))
    if n < 0:
        contador += 1
    cntl += 1
print(f"tem {contador} números negativos!")
