#11)Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
#celsius = (F-32) / 1.8 
#Observação: Para testar se a sua resposta está correta saiba que 100℃ = 212F
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"A temperatura em Celsius é: {celsius:.2f}")
