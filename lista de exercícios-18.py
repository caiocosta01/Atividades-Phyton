#18. Ler 80 números e ao final informar quantos número (s) est (á) ão no intervalo entre 10 (inclusive) e 150 (inclusive).
contro = 0
contador = 0
while contro < 8:
    n = float(input("informe um número: "))
    contro += 1
    if n >= 10 and n <= 150:
        contador += 1
print(f"estão no intervalo {contador} números!")
    
    