#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
""" O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” 
se o conceito for D ou E. """
"""   Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E """
# A atribuição de conceitos obedece à tabela abaixo:

tabela_notas = """   
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0           A
Entre 7.5 e 9.0            B
Entre 6.0 e 7.5            C
Entre 4.0 e 6.0            D
Entre 4.0 e 0.0            E """

print(tabela_notas)


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

if media > 10 or media < 0:
  print("Média inválida")
elif media >= 9.0:
  print(f"NOTA A ,primeira nota: {n1:.2f}, segunda nota: {n2:.2f}, média: {media:.2f} “APROVADO”")
elif media >= 7.5:
  print(f"NOTA B ,primeira nota: {n1:.2f}, segunda nota: {n2:.2f}, média: {media:.2f} “APROVADO”")
elif media >= 6.0:
  print(f"NOTA C ,primeira nota: {n1:.2f}, segunda nota: {n2:.2f}, média: {media:.2f} “APROVADO”")
elif media >= 4.0:
  print(f"NOTA D ,primeira nota: {n1:.2f}, segunda nota: {n2:.2f}, média: {media:.2f} “REPROVADO”")
elif media >= 0:
  print(f"NOTA E ,primeira nota: {n1:.2f}, segunda nota: {n2:.2f}, média: {media:.2f} “REPROVADO”")








