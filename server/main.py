from server import Server
from game_model import Game

from pygame.time import Clock
from time import time

server_host = '127.0.0.1'
server_port = 2056


def main():
    server = Server(server_host, server_port)
    main_loop(server)


# основной двигатель игры
def main_loop(server):
    game_model = Game()

    server.get_events_buffer(server_host, server_port)
    # FIXME убрать за необходимостью
    # control_event = self.control_events.pop(-1)
    # player_event = self.player_events.pop(-1)

    start_record = time()
    server_tick = Clock()
    event = (None, None)

    while server.alive:
        server_tick.tick(60) # 60 кадров в секунду
        event = (None, None)

        if server.control_events:
            event = server.control_events.pop(-1) # сначала отправляется (команда (ip, port))
            gamer_addr = event[1]

            # добавляем игрока в модель игры
            if event[0] == b'HI':
                pass

            # игрок сообщает серверу, что он подключен
            elif event[0] == b'ONLINE':
                pass # обновляем время игрока

            # удаляем игрока, т.к. он закрыл клиента
            elif event[0] == b'DIS':
                pass # удаляем игрока из модели игры

            # спавним игрока при нажатии enter
            elif event[0] == b'SPAWN':
                pass

        if server.player_events: # расположение и команды и id
            event = server.player_events.pop(-1)
            event = (event[0], (event[1][0], event[1][1] - 1))

        # обрабатываем события

        # удаляем тех у кого пропало соединение

        # если игрока нет больше n сек, то нах выкидываем его


if __name__=='__main__':
    main()