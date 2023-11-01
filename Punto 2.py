# Resolucion del segundo ejercisio de laboratorio 1
# Cajero Automático
tarjetas = [{"numero": "1234567890", "clave": "1234", "saldo": 10000}, 
            {"numero": "0987654321", "clave": "4321", "saldo": 5000},
            {"numero": "5678901234", "clave": "5678", "saldo": 20000}]

numero_ingresado = input("Ingrese número de tarjeta: ")

tarjeta_encontrada = False
for tarjeta in tarjetas:
    if tarjeta["numero"] == numero_ingresado:
        tarjeta_encontrada = True
        clave_ingresada = input("Ingrese clave: ")
        if tarjeta["clave"] == clave_ingresada:
            if tarjeta["saldo"] >= 10000:
                monto = int(input("Ingrese monto a retirar: "))
                if monto <= tarjeta["saldo"]:
                    tarjeta["saldo"] -= monto
                    print("Retiro realizado.")
                    print("Nuevo saldo:", tarjeta["saldo"])
                else:
                    print("Monto a retirar excede el saldo.")
            else:
                print("Saldo insuficiente para retirar.")
        else:
            print("Clave incorrecta.")
        break

if not tarjeta_encontrada:
    print("Número de tarjeta inválido.")