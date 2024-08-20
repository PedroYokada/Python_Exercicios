#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Insira uma letra, o programa vai dizer se é vogal ou consoante: ")

if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
  print(f"A letra digitada {letra} é uma vogal.")
else:
  print(f"A letra digitada {letra} é uma consoante.")