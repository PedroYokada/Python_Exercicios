#Faça um programa que calcule o mostre a média aritmética de N notas.

n = 1
soma_notas = 0
media = 0

while n == 1:
  nota = float(input("Insira um valor de uma nota: "))
  soma_notas = float(nota + soma_notas)
  media += 1
  n = int(input("Deseja somar mais uma nota? 1-Sim/2-Não: "))
  
print(f"A média total é de: {soma_notas/media:.2f}")
  