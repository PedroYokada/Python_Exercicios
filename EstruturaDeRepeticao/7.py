#Faça um programa que leia 5 números e informe o maior número.

num = 1

while num <= 5:
  num = 1 + num
  print(num - 1)
  
print(f"O maior numero é: {num - 1}")

num1 = int(input("Insira um numero: "))

for i in range(5):
  valor_final = num1 + 1 + i
  print(valor_final)
  
print(f"O maior numero é: {valor_final}")