#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Insira um numero: "))

if num < 0:
  print(f"O numero {num:.2f} é negativo.")
elif num == 0:
   print(f"O numero {num:.2f} é neutro.")
else:
   print(f"O numero {num:.2f} é positivo")