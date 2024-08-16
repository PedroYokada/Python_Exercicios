#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

inteiro1 = int(input("Insira o primeiro numero inteiro: "))
inteiro2 = int(input("Insira o segundo numero inteiro: "))
real1 = float(input("Insira um numero real: "))

produto_dobro_primeiro = float((2 * inteiro1) * (inteiro2/2))
produto_dobro_primeiro = round(produto_dobro_primeiro,2)

soma_triplo = float((3*inteiro1) + real1)
soma_triplo = round(soma_triplo,2)

terceiro_elevado = float(real1**3)
terceiro_elevado = round(terceiro_elevado,2)

print("o produto do dobro do primeiro numero com metade do segundo numero é de:  ", produto_dobro_primeiro)
print("a soma do triplo do primeiro numero com o terceiro numero é de: ", soma_triplo)
print("o terceiro numero elevado ao cubo é de:: ", terceiro_elevado)
