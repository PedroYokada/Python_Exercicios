#Faça um Programa que leia três números e mostre o maior e o menor deles.

# inserir os numeros
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))
num3 = float(input("Insira o terceiro numero: "))

# condições de qual é o maior numero
if num1 > num2 and num1 > num3:
  print(f"O maior numero é: {num1}")
elif num2 > num1 and num2 > num3:
  print(f"O maior numero é: {num2}")
else:
  print(f"O maior numero é: {num3}")

# condições de qual é o menor numero

if num1 < num2 and num1 < num3:
  print(f"O menor numero é: {num1}")
elif num2 < num1 and num2 < num3:
  print(f"O menor numero é: {num2}")
else:
  print(f"O menor numero é: {num3}")