import xmlrpc.client  # Cliente RPC en Python

# Conectarse al servidor RPC en localhost:8000
servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Función para interactuar con el usuario
def calcular():
    print("\n📌 Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("👉 Ingresa el número de la operación: ")

    if opcion == "5":
        print("🔴 Saliendo del cliente RPC...")
        return False

    if opcion in ["1", "2", "3", "4"]:
        try:
            a = float(input("🔢 Ingresa el primer número: "))
            b = float(input("🔢 Ingresa el segundo número: "))

            if opcion == "1":
                resultado = servidor.sumar(a, b)
                operacion = "Suma"
            elif opcion == "2":
                resultado = servidor.restar(a, b)
                operacion = "Resta"
            elif opcion == "3":
                resultado = servidor.multiplicar(a, b)
                operacion = "Multiplicación"
            elif opcion == "4":
                resultado = servidor.dividir(a, b)
                operacion = "División"

            print(f"✅ Resultado de la {operacion}: {resultado}")

        except Exception as e:
            print(f"❌ Error: {e}")

    else:
        print("⚠️ Opción inválida, intenta de nuevo.")

    return True

# Ejecutar interactivamente hasta que el usuario decida salir
while calcular():
    pass
