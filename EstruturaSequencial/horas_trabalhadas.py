#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

valor_hora = float(input("Insira o valor da hora trabalhada: "))
Numhora_trabalhada = float(input("Insira a quantidade de horas trabalhadas: "))

salario = float(valor_hora * Numhora_trabalhada)
salario = round(salario, 2)

print("O salario bruto é de: ", salario, "R$")

imposto_renda = float((salario * 0.11))
imposto_renda = round(imposto_renda, 2)

print("O valor do imposto de renda é de: ", imposto_renda, "R$")

inss = float((salario * 0.08))
inss = round(inss, 2)

print("O valor do INSS é de: ", inss, "R$")

taxa_sindicato = float((salario * 0.05))
taxa_sindicato = round(taxa_sindicato, 2)

print("O valor da taxa do sindicato é de: ", taxa_sindicato, "R$")

salario_liquido = float(salario - (imposto_renda + inss + taxa_sindicato))
salario_liquido = round(salario_liquido, 2)

print("O salario liquido é de: ", salario_liquido, "R$")