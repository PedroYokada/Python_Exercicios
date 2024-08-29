""" Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação. """


decisao = "s"

while decisao == "s":
  
  num_anos = 0
  
  paisA = float(input("Insira o numero da população do Páis A: "))
  paisB = float(input("Insira o numero da população do Páis B: "))
  taxaA = float(input("Insira a taxa de crescimento do Páis A: "))/100
  taxaB = float(input("Insira a taxa de crescimento do Páis B: "))/100
  
  while paisA < paisB:
      paisA += paisA * taxaA
      paisB += paisB * taxaB
      num_anos += 1
      
  print(f"A população do País A é de: {paisA:.2f} habitantes")
  print(f"A população do País B é de: {paisB:.2f} habitantes")
  print(f"O número de anos para o País A superar o País B é de: {num_anos} anos")
 
  decisao = input("Deseja realizar a operação novamente? (s/n): ").upper()
  if decisao == 'N':
      print("Fim do programa!")
      break
    


