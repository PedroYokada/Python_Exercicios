#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = float(input("Insira o valor da largura: "))

area_quadrado = (largura * largura)

area_quadrado = round(area_quadrado, 2)

print("Area do quadrado = ", area_quadrado)

dobro_area = float(area_quadrado * area_quadrado)

dobro_area = round(dobro_area, 2)

print("o dobro da area do quadrado é = ", dobro_area)