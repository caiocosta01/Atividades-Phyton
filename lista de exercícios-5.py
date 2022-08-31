#5. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
c = float(input("informe a temperatura em graus Celcius para a conversão: "))
f = (9*c+160)/5
print(f"a temperatura em graus Fahrenheit é: {round(f,2)}")