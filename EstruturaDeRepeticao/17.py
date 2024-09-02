# Faça um programa que calcule o fatorial 
# e um número inteiro fornecido pelo usuário


fatorial = 1
num = int(input("Insira um numero para o calculo de fatorial: "))

for x in range(1, num + 1):
  fatorial *= x
  
print(f"O resultado do fatorial é de: {fatorial:.2f}")

      
