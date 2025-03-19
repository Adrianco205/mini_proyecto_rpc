from xmlrpc.server import SimpleXMLRPCServer  # Servidor RPC en Python

# Crear el servidor en localhost y puerto 8000
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC en ejecución en el puerto 8000...")

# Definir múltiples funciones remotas
def sumar(a, b):
    print(f"Sumando {a} + {b}")
    return a + b

def restar(a, b):
    print(f"Restando {a} - {b}")
    return a - b

def multiplicar(a, b):
    print(f"Multiplicando {a} * {b}")
    return a * b

def dividir(a, b):
    if b == 0:
        print("Error: División por cero")
        return "Error: División por cero"
    print(f"Dividiendo {a} / {b}")
    return a / b

# Registrar funciones en el servidor
server.register_function(sumar, "sumar")
server.register_function(restar, "restar")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

# Iniciar servidor
server.serve_forever()
