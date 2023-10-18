try:
    x= int(input("Ingresa el valor de X: "))
except ValueError:
    print(" x NO es un entero")
else:
    print("El valor de x es:",x)