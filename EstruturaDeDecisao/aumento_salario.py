""" As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento. """

salario = float(input("Insira o valor do salario em R$: "))
print(f"O valor do salario sem reajuste é de: {salario:.2f}" )

if salario <= 280.00:
  salario_reajustado = float(salario + (salario * 0.2))
  print("O percentual de aumento é de 20%" )
  print(f"O valor do aumento é de: {salario * 0.2}" )
  print(f"O salario reajustado é de: {salario_reajustado:.2f}")
elif salario > 280.00 and salario <= 700.00:
  salario_reajustado = float(salario + (salario * 0.15))
  print("O percentual de aumento é de 15%" )
  print(f"O valor do aumento é de: {salario * 0.15}" )
  print(f"O salario reajustado é de: {salario_reajustado:.2f}")
elif salario > 700.00 and salario <= 1500.00:
  salario_reajustado = float(salario + (salario * 0.1))
  print(f"O valor do aumento é de: {salario * 0.1}" )
  print("O percentual de aumento é de 10%" )
  print(f"O salario reajustado é de: {salario_reajustado:.2f}")
else:
  salario_reajustado = float(salario + (salario * 0.05))
  print("O percentual de aumento é de 5%" )
  print(f"O valor do aumento é de: {salario * 0.05}" )
  print(f"O salario reajustado é de: {salario_reajustado:.2f}")