#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite M-matutino ou V-Vespertino ou N- Noturno: ")

if turno == "m" or turno == "M":
  print("Bom Dia!")
elif turno == "v" or turno == "V":
  print("Boa Tarde!")
elif turno == "n" or turno == "N":
  print("Boa Noite!")
else:
  print("Valor Inválido!")
