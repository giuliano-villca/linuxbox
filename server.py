import socket

preguntas = [
    {
        "pregunta": "1) ¿En que puesto quedaron los muchachos de la confederacion suiza en la final nacional copa robotica 2025?",
        "opciones": ["a) Primer lugar", "b) Segundo lugar", "c) Tercer lugar", "d) Cuarto lugar"],
        "respuesta": "c"
    },
    {
        "pregunta": "2) ¿En que pais se origina tiktok?",
        "opciones": ["a) EEUU", "b) China", "c) taiwan", "d) australia "],
        "respuesta": "b"
    },
    {
        "pregunta": "3) ¿que pais gano el mundial  2018?",
        "opciones": ["a) Bolivia", "b) Croacia", "c) Francia", "d) alemania"],
        "respuesta": "c"
    },
    {
        "pregunta": "4) ¿Que tipo de pokemon es Jigglypuff?",
        "opciones": ["a) normal", "b) normal y hada", "c) hada", "d) normal y veneno"],
        "respuesta": "b"
    },
    {
        "pregunta": "5) ¿Cual de estas cartas vale 6 de elixis?",
        "opciones": ["a) los reclutas reales", "b) Goblinstein", "c) Gigante rúnico", "d) Recolecto de elixis"],
        "respuesta": "d"
    }
]

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, 12345))
server_socket.listen(1)

print(f"Servidor escuchando en {ip}:12345")

while True:
    client_socket, address = server_socket.accept()
    print("Conexión establecida con:", address)

    client_socket.send("Bienvenido al formulario.\n".encode())

    client_socket.send("Ingrese su nombre: ".encode())
    nombre = client_socket.recv(1024).decode()

    puntaje = 0

    for p in preguntas:
        texto = p["pregunta"] + "\n" + "\n".join(p["opciones"]) + "\nTu respuesta: "
        client_socket.send(texto.encode())
        respuesta = client_socket.recv(1024).decode().strip().lower()

        if respuesta == p["respuesta"]:
            puntaje += 1

    resultado = f"{nombre}, tu puntaje final es {puntaje}/{len(preguntas)}"
    client_socket.send(resultado.encode())

    client_socket.close()