#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Digite um numero inteiro ou decimal: "))

if num == round(num):
  print(f"o numero {num} é inteiro!")
else:
  print(f"o numero {num} é decimal!")