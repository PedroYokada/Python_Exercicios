#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Insira F - Feminino, M - Masculino: ")

if sexo == "f" or sexo == "F":
  print("Sexo Feminino.")
elif sexo == "m" or sexo == "M":
  print("Sexo Masculino.")
else:
  print("Sexo inválido.")