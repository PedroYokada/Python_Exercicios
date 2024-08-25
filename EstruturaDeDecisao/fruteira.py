""" Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """

ate5kg_morango = 2.50
maior5kg_morango = 2.20
ate5kg_maca = 1.80
maior5kg_maca = 1.50

morango = float(input("Quantos kilos de morango você deseja ?: "))

maca = float(input("Quantos kilos de maça você deseja ?: "))

if morango <= 5:
  preco_morango = ate5kg_morango * morango
else:
  preco_morango = maior5kg_morango * morango
  
if maca <= 5:
  preco_maca = ate5kg_maca * maca
else:
   preco_maca = maior5kg_maca * maca
   
preco_final = preco_maca + preco_morango


if preco_final > 25.00 or (maca + morango) > 8:
  preco_final = preco_final - (preco_final * 0.1)
  

print(f"O valor da compra é de: {preco_final:.2f}R$")


   

  
  
 




 
