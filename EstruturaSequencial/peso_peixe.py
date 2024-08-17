#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Insira o peso do peixe: "))
excesso = float(peso_peixe - 50)
excesso = round(excesso, 2)

if excesso <= 0:
  print("Não tera que pagar multa excedente de peso do peixe.")
else:
  print("O valor do peso exedente do peixe é de: ", excesso , "Kg" )
  multa = float(4.0 * excesso) 
  multa = round(multa, 2)
  print("O valor do da multa é de: ", multa , "R$" )
