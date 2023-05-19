import pandas as pd

inicio = int(input("Ingresa año inicial: "))
fin = int(input("Ingresa año final: "))
ventas = {}
for i in range(inicio, fin + 1):
    ventas[1] = float(input("Ingresa la ganancia del año: " + str(i) + ": "))
ventas = pd.Series(ventas)
print("ventas\n", ventas)
print("ventas con descuento\n", ventas * 0.9)
