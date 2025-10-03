import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, 12345))

mensaje = client_socket.recv(1024).decode()
print(mensaje)


nombre_pedido = client_socket.recv(1024).decode()
nombre = input(nombre_pedido)
client_socket.send(nombre.encode())


for _ in range(5):
    pregunta = client_socket.recv(1024).decode()
    respuesta = input(pregunta)
    client_socket.send(respuesta.encode())

resultado = client_socket.recv(1024).decode()
print("\n" + resultado)

client_socket.close()

