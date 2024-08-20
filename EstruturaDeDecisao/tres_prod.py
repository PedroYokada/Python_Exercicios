#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Insira o valor do primeiro produto : "))
prod2 = float(input("Insira  o valor do segundo produto : "))
prod3 = float(input("Insira o valor do terceiro produto : "))

if prod1 < prod2 and prod1 < prod3:
  print(f"O produto mais barato é o primeiro produto, o custo dele é de {prod1:.2f} R$.")
elif prod2 < prod1 and prod2 < prod3:
  print(f"O produto mais barato é o segundo produto, o custo dele é de {prod2:.2f}  R$.")
else:
  print(f"O produto mais barato é o terceiro produto, o custo dele é de {prod3:.2f} R$.")