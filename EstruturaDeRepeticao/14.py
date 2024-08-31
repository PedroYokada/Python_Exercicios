#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

soma_par = 0
soma_impar = 0
num = 0

for i in range(0,10):
  num = int(input("Insira um numero: "))
  if num % 2 != 0:
    soma_par += 1
  else:
    soma_impar += 1

print(f"A soma de numeros pares é de: {soma_par}")
print(f"A soma de numeros impares é de: {soma_impar}")
    
 