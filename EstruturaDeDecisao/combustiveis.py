""" Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. """

litros = 0
preco_alc = 1.90
preco_gas = 2.50
preco_final = 0

tipo_combustivel = input("Escolha o combustivel A = Álcool / G = Gasolina: ").strip().upper()

if tipo_combustivel == "A":
  litros = float(input("Quantos litros de Álcool?: "))
  
  if litros <= 20:
    preco_final = float((litros * preco_alc) - (0.03 * litros * preco_alc))
    print(f"Preço final  dos litros de Álcool: {preco_final:.2f}")
  elif litros > 20:
    preco_final = float((litros * preco_alc) - (0.05 * litros * preco_alc))
    print(f"Preço final dos litros de Álcool: {preco_final:.2f} ")

elif tipo_combustivel == "G":
  litros = float(input("Quantos litros de Gasolina?: "))
  
  if litros < 20 or litros == 20:
    preco_final = float((litros * preco_gas) - (0.04 * litros * preco_gas))
    print(f"Preço final dos litros de Gasolina: {preco_final:.2f} ")
  elif litros > 20:
    preco_final = float((litros * preco_gas) - (0.06 * litros * preco_gas))
    print(f"Preço final dos litros de Gasolina: {preco_final:.2f} ")
else:
  print("Operação Inválida")