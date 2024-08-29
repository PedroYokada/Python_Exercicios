#Faça um programa que leia 5 números e informe a soma e a média dos números.
somaN = 0
m = 0
n = 0


for i in range(5):
  n = float(input("Insira um numero: "))
  m = 1 + m
  somaN += n

print(f"A soma dos numeros é de: {somaN:.2f}")
print(f"A média dos numeros é de: {somaN/m:.2f}")
  
