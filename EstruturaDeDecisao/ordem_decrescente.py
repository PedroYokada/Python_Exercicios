#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))
num3 = float(input("Insira o terceiro numero: "))

if num1 < num2 < num3:
  print(f"{num1:.2f} , {num2:.2f}, {num3:.2f} ")
elif num1 < num3 < num2:
  print(f"{num1:.2f} , {num3:.2f}, {num2:.2f} ")
elif num2 < num1 < num3:
  print(f"{num2:.2f} , {num1:.2f}, {num3:.2f} ")
elif num2 < num3 < num1:
  print(f"{num2:.2f} , {num3:.2f}, {num1:.2f} ")
elif num3 < num1 < num2:
  print(f"{num3:.2f} , {num1:.2f}, {num2:.2f} ")
else:
  print(f"{num3:.2f} , {num2:.2f}, {num1:.2f} ")