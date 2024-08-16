#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hora_valor = float(input("Quanto você ganha por hora ?:"))
trabalho_horas = int(input("Quantas horas trabalhadas você tem?:"))

salario_trabalhador = float((hora_valor * trabalho_horas))
salario_trabalhador = round(salario_trabalhador,2)

print("Seu salario é de: ", salario_trabalhador, "R$")



