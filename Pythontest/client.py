import socket

HOST = '127.0.0.1'
PORT = 5000


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Conectado al servidor. Escribe tu mensaje.")

        while True:
            message = input("Tú: ")
            client_socket.sendall(message.encode('utf-8'))
            if message.upper() == "DESCONEXION":
                print("Desconectando del servidor...")
                break
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Servidor: {response}")


if __name__ == "__main__":
    start_client()
