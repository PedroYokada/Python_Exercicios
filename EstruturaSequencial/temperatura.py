#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
f = float(input("Digite a temperatura em Fahrenheit: "))
f = C = 5 * ((f-32) / 9)
C = round(C, 2)

print("A temperatura em celsius equivale a: ", C, "°C")