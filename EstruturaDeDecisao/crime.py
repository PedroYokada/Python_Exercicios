""" Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente". """

soma_perguntas = 0
pergunta1 = input("Telefonou para a vítima? Sim = S/ Não = N: ").strip().upper()

##.strip().upper() transforma as letras minusculas em maisculas.

if pergunta1 == "S": 
  soma_perguntas += 1
elif pergunta1 == "N": 
  soma_perguntas += 0
else:
  print("Operação inválida")
 
pergunta2 = input("Esteve no local do crime? Sim = S/ Não = N: ").strip().upper()

if pergunta2 == "S":
  soma_perguntas += 1
elif pergunta2 == "N":
  soma_perguntas += 0
else:
  print("Operação inválida: ")

pergunta3 = input("Mora perto da vítima? Sim = S/ Não = N :").strip().upper()

if pergunta3 == "S":
  soma_perguntas += 1
elif pergunta3 == "N":
  soma_perguntas += 0
else:
  print("Operação inválida: ")

pergunta4 = input("Devia para a vítima? Sim = S/ Não = N: ").strip().upper()

if pergunta4 == "S":
  soma_perguntas += 1
elif pergunta4 == "N":
  soma_perguntas += 0
else:
  print("Operação inválida: ")

pergunta5 = input("Já trabalhou com a vítima? Sim = S/ Não = N: ").strip().upper()

if pergunta5 == "S":
  soma_perguntas += 1
elif pergunta5 == "N":
  soma_perguntas += 0
else:
  print("Operação inválida: ")
  
print(f"Total de respostas 'Sim': {soma_perguntas}")

if soma_perguntas == 2:
  print("Suspeita")
elif soma_perguntas >= 3 and  soma_perguntas <= 4:
 print("Cúmplice")
elif soma_perguntas <= 1:
  print("Inocente")
else:
  print("Assassino")