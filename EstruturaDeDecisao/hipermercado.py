""" O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de 
carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, 
preço total, tipo de pagamento, valor do desconto e valor a pagar. """

file_ate5 = 4.90
file_mais5 = 5.80
alcatra_ate5 = 5.90
alcatra_mais5 = 6.80
picanha_ate5 = 6.90
picanha_mais5 = 7.80

tipo_carne = input("Escolha um tipo de carne, F:Filé Duplo/A:Alcatra/P:Picanha: ").strip().upper()

match tipo_carne:
    case "F":
        qnt_carne = float(input("Digite a quantidade em Kg: "))
        if qnt_carne <= 5:
          compra = qnt_carne * file_ate5
        else:
          compra = qnt_carne * file_mais5
        
        forma_pagamento = input("Qual a forma de pagamento ? C-Cartão/O-Outros: ").strip().upper()
        
        if forma_pagamento == "C":
          compra = compra - (compra * 0.05)
          print(f"O tipo da carne é: Filé duplo.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Cartão Tabajara.")
          print(f"O desconto da compra é de 5%.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        elif forma_pagamento == "O":
          print(f"O tipo da carne é: Filé duplo.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Outros.")
          print(f"Não tem desconto, é exclusivo do pagamento em cartão.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        else:
          print("Forma de pagamento inválida.")
          exit()
    case "A":
        qnt_carne = float(input("Digite a quantidade em Kg: "))
        if qnt_carne <= 5:
          compra = qnt_carne * alcatra_ate5
        else:
          compra = qnt_carne * alcatra_mais5
          
        forma_pagamento = input("Qual a forma de pagamento ? C-Cartão/O-Outros: ").strip().upper()
        
        if forma_pagamento == "C":
          compra = compra - (compra * 0.05)
          print(f"O tipo da carne é: Alcatra.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Cartão Tabajara.")
          print(f"O desconto da compra é de 5%.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        elif forma_pagamento == "O":
          print(f"O tipo da carne é: Alcatra.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Outros.")
          print(f"Não tem desconto, é exclusivo do pagamento em cartão.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        else:
          print("Forma de pagamento inválida.")
          exit()
         
    case "P":
        qnt_carne = float(input("Digite a quantidade em Kg: "))
        if qnt_carne <= 5:
          compra = qnt_carne * picanha_ate5
        else:
          compra = qnt_carne * picanha_mais5
        
        forma_pagamento = input("Qual a forma de pagamento ? C-Cartão/O-Outros: ").strip().upper()
        
        if forma_pagamento == "C":
          compra = compra - (compra * 0.05)
          print(f"O tipo da carne é: Picanha.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Cartão Tabajara.")
          print(f"O desconto da compra é de 5%.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        elif forma_pagamento == "O":
          print(f"O tipo da carne é: Picanha.")
          print(f"A quantidade de carne foi de: {qnt_carne:.2f}Kg")
          print(f"A forma de pagamento foi: Outros.")
          print(f"Não tem desconto, é exclusivo do pagamento em cartão.")
          print(f"O valor total da compra é de: {compra:.2f}R$")
          exit()
        else:
          print("Forma de pagamento inválida.")
          exit()
    case _:
        print("Tipo de carne inválido.")
        exit()