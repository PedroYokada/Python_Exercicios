#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo  = float(input("Insira o tamanho do arquivo para download (em MB): "))
velocidade  = float(input("Insira a velocidade de download (em Mbps): "))

tempo_download = float((arquivo * 8)/(velocidade * 60))
tempo_download = round(tempo_download, 2)

print(f"O tempo de download é de: , {tempo_download:.2f}, min")