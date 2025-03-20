#05 As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("quantas maças foram compradas?")
macas = int(input())
valor=0
if macas < 12:
    valor=1.3
else:
    valor=1.0
    
macas*valor
print("o valor gasto é:",macas*valor)
