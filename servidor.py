from xmlrpc.server import SimpleXMLRPCServer #permite crear un servidor RPC en Python.

# Crear el servidor en localhost y puerto 8000
server = SimpleXMLRPCServer(("localhost", 8000))

# Definir la función remota
def sumar(a, b):
    return a + b

# Registrar la función en el servidor para que pueda ser llamada por un cliente
server.register_function(sumar, "sumar")

print("Servidor RPC en ejecución en el puerto 8000...")
server.serve_forever()  # Mantiene el servidor activo
