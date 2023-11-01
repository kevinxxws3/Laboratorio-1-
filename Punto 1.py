# Resolucion del primer ejercisio de laboratorio 1
# Comprobación de suma de dígitos

import random

def generar_numero_aleatorio():
    return random.randint(10000, 99999)

def suma_digitos(numero):
    numero_str = str(numero)
    primeros_tres = [int(digito) for digito in numero_str[:3]]
    ultimos_dos = [int(digito) for digito in numero_str[3:]]
    suma_primeros_tres = sum(primeros_tres)
    suma_ultimos_dos = sum(ultimos_dos)
    return suma_primeros_tres, suma_ultimos_dos

def comprobar_suma_digitos(numero):
    suma_primeros_tres, suma_ultimos_dos = suma_digitos(numero)
    if suma_primeros_tres == suma_ultimos_dos:
        return "La comprobación es válida."
    else:
        return "La comprobación no es válida."

numero_aleatorio = generar_numero_aleatorio()
print(f"Número aleatorio generado: {numero_aleatorio}")
resultado = comprobar_suma_digitos(numero_aleatorio)
print(resultado)



