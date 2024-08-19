#Faça um Programa que peça dois números e imprima o maior deles.

v1 = int(input("Insira o primeiro numero: "))
v2 = int(input("Insira o segundo numero: "))


if v1 > v2:
  print(f"O maior valor entre os dois é {v1:.2f} ")
else:
   print(f"O maior valor entre os dois é {v2:.2f} ")