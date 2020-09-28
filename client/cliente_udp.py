from socket import socket, AF_INET, SOCK_DGRAM


class UDPClient:
    def __init__(self):
        self.__socket = socket(AF_INET, SOCK_DGRAM)

        while True:
            message = input()
            self.__socket.sendto(message.encode(), ('localhost', 9500))


if __name__ == "__main__":
    udp_client = UDPClient()

