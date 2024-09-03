#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

valores_somados_cds = 0

qnt_cds = int(input("Insira a quantidade de CD's: "))

for i in range (0,qnt_cds):
  valor_cd = float(input(f"Insira o valor do CD {i + 1}: "))
  valores_somados_cds += valor_cd
  
media = valores_somados_cds/qnt_cds

print(f"O preço medio dos CD's é de: {media:.2f}R$")