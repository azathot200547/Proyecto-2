#Calcular IMC

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Su IMC es {imc:.2f}")
print(f"Usted se encuentra en la categoria de {categoria}")
