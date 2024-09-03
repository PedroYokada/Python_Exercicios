#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos
# para cada turma. As turmas não podem ter mais de 40 alunos.

soma_alunos_turmas = 0
qnt_turmas = int(input("Insira a quantidade de turmas: "))

for x in range(0,qnt_turmas):
  qnt_alunos_turma = int(input(f"Insira a quantidade de alunos da turma {x + 1}: "))
  
  if qnt_alunos_turma < 1 or qnt_alunos_turma > 40:
    print("Quantidade inválida!, o numero de alunos deve ser entre 1 a 40!")
  else:
    soma_alunos_turmas += qnt_alunos_turma
    
if qnt_turmas > 0:  
  media = soma_alunos_turmas/qnt_turmas
  print(f"A soma de alunos de todas as turmas é de: {soma_alunos_turmas:.2f}")
  print(f"A media de alunos por turma é de: {media:.2f}")
else:
  print(f"Não tem turmas, portanto não tem alunos!")