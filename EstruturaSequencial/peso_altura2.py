#Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
# algoritmo que calcule seu peso ideal, utilizando as 
# seguintes fórmulas
#Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

caracter = input("Insira H para homem ou M para mulher: ")

if caracter == "h" or caracter ==  "H":
  altura_homem = float(input("Insira a altura deste homem: "))
  peso_ideal_homem = float((72.7*altura_homem) - 58)
  peso_ideal_homem  = round(peso_ideal_homem ,2)
  print("O peso ideal deste homem é de: ", peso_ideal_homem, "kg")
elif caracter == "m" or caracter ==  "M":
  altura_mulher = float(input("Insira a altura desta mulher: "))
  peso_ideal_mulher = float((62.1*altura_mulher) - 44.7)
  peso_ideal_mulher = round(peso_ideal_mulher,2)
  print("O peso ideal desta mulher é de: ", peso_ideal_mulher, "kg")
else:
  print("Operação Inválida")
