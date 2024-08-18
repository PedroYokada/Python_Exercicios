#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros_quadrados = float(input("Insira a quantidade de metros quadrados: "))

litros = float(metros_quadrados / 3)

latas = float(litros / 18)

preco_final = float(latas * 80.00)

print(f"O preço total é de da tinta é de: {preco_final:.2f}", "R$")
