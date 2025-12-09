import socket

HOST = "0.0.0.0"
PORT = 8080

# Cria o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor rodando em http://localhost:{PORT}")

while True:
    conn, addr = server.accept()
    print("Conexão recebida de:", addr)

    # Lê a requisição (apenas primeira linha)
    request = conn.recv(1024).decode()
    first_line = request.split("\n")[0]
    print("Primeira linha da requisição:", first_line)

    # Resposta HTTP mínima
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 13\r\n"
        "\r\n"
        "Olá Mundo!!!"
    )

    conn.sendall(response.encode())
    conn.close()
