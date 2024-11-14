# Programa Peso Ideal
altura = float(input("Informe a sua altura(metros): "))
homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7
print(f"O peso ideal para os homens é {homens:.2f} Kg, enquanto para mulheres é {mulheres:.2f} Kg.")
