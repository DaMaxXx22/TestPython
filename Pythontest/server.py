import socket

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Conexión establecida con {addr}")
            with client_socket:
                while True:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    print(f"Recibido de cliente: {data}")
                    if data.upper() == "DESCONEXION":
                        print("Cliente solicitó desconexión.")
                        break
                    response = data.upper()
                    client_socket.sendall(response.encode('utf-8'))
            print(f"Conexión con {addr} cerrada.\n")

if __name__ == "__main__":
    start_server()
