def calcular_percentuais(votos_brancos, votos_nulos, votos_validos, total_eleitores):
    
    percentual_brancos = (votos_brancos / total_eleitores) * 100
    percentual_nulos = (votos_nulos / total_eleitores) * 100
    percentual_validos = (votos_validos / total_eleitores) * 100
    return percentual_brancos, percentual_nulos, percentual_validos
total_eleitores = int(input("Qual o total de eleitores? "))
votos_brancos = int(input("Qual a quantidade de votos brancos? "))
votos_nulos = int(input("Quantos votos nulos? "))
votos_validos = int(input("Quantos votos válidos? "))

percentual_brancos, percentual_nulos, percentual_validos = calcular_percentuais(votos_brancos, votos_nulos, votos_validos, total_eleitores)

print(f"Total de votos válidos: {percentual_validos:.2f}%")
print(f"Total de votos em branco: {percentual_brancos:.2f}%")
print(f"Total de votos nulos: {percentual_nulos:.2f}%")
