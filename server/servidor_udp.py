from socket import socket, AF_INET, SOCK_DGRAM


class UDPSever:
    def __init__(self, address, port):
        self.__server_socket = socket(AF_INET, SOCK_DGRAM)
        self.__server_socket.bind((address, port))
        self.__max_players = 0
        self.__players = []

    def __ad_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            self.__max_players += 1

    def start_server(self):
        while self.__max_players <= 5:
            data, client_address = self.__server_socket.recvfrom(2048)
            print(f'The client {client_address} send >>> {data.decode()}')
            self.__server_socket.sendto("olá".encode(), client_address)
            self.__ad_player(client_address)

        print(self.__players)


if __name__ == "__main__":
    udp_server = UDPSever('localhost', 9500)
    udp_server.start_server()
