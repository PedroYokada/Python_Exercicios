""" Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 """



valor_hora = float(input("Insira o valor que você ganha por hora em R$: "))
qntd_horas = int(input("Insira quantas horas você trabalha: "))

salario_bruto = float(valor_hora * qntd_horas)

if salario_bruto <= 900.00:
  print("Isento de Imposto de renda")
elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
  desconto_renda =  salario_bruto * 0.05
elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
  desconto_renda =  salario_bruto * 0.10
else:
  desconto_renda =  salario_bruto * 0.20
 

  salario_liquido = salario_bruto - desconto_renda

  desconto_sind = float(salario_bruto * 0.03)
  fgts = float(salario_bruto * 0.11)
  desconto_inss = float(salario_bruto * 0.10)
  descontos_totais = salario_bruto - (desconto_inss + desconto_sind + desconto_renda)
  salario_liquido = salario_bruto - descontos_totais







