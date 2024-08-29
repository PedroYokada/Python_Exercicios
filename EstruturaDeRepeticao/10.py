#Faça um programa que receba dois números inteiros e gere os números 
# inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Insira um numero inteiro: "))
n2 = int(input("Insira outro inteiro: "))


primeiro = n1
segundo = n2

for i in range(primeiro,segundo + 1):
  print(i)