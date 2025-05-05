#ejercicio 18
numero = int(input("Ingresa un número entero: "))

suma = 0
for i in range(1, 101):  
    suma += numero + i

print(f"La suma de los 100 números siguientes a {numero} es: {suma}")

def euros_a_dolares (euros,tasa_cambio):

    dolares= euros * tasa_cambio

    return dolares

euros= float(input("ingrese la cantidad de euros:"))
tasa_cambio= float(input()"ingrese la tasa de cambio(1 euro =?)")