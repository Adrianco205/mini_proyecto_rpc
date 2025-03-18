import xmlrpc.client #permite al cliente comunicarse con el servidor.

# Conectarse al servidor RPC
servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Llamar la función remota
resultado = servidor.sumar(5, 7)

# Imprimir el resultado
print(f"Resultado de la suma: {resultado}")
