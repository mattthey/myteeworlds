from game_model import Game

from time import time
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread, Lock


class Server:
    def __init__(self, host, port):
        self.proc_threading_list = [] # FIXME убрать
        self.host = host
        self.port = port
        self.alive = True
        self.server_work_time = time()
        self.control_events = []
        self.player_events = []

    # создаем два потока для чтени данных и записываем в control_events и player_events
    def get_events_buffer(self, server_host, server_port):

        connection_for_recive_control_event = Thread(
            target=self.connection_server_reciver,
            args=(server_host, server_port, self.control_events)
        )

        connection_for_recive_player_event = Thread(
            target=self.connection_server_reciver,
            args=(server_host, server_port + 1, self.player_events)
        )

        connection_for_recive_control_event.start()
        connection_for_recive_player_event.start()

    # здесь описана передача входных данных в процесс, на который прокинута труба
    # данные приходят на какой-то хост/порт, а мы к нему здесь подсасываемся, и слушаем его
    def connection_server_reciver(self, events):
        server_addr = (self.host, self.port)
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        udp_socket.bind(server_addr)
        try:
            while True:
                events.append(udp_socket.recvfrom(128))
        except:
            udp_socket.close()

    # TODO поток для отправки данных