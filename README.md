# MYTEEWORLDS

Структура проекта myteeworlds:
* client
    * __main.py__
        ###### TODO расписать эту поеботу тоже
        
* server
    * __main.py__ - для запуска проекта
        * создает переменную сервер
        * запускает сервер
    
    * __server.py__ - контроллер для server_model.py
        * класс _Server_ с методами:
            * _init_ инициализация модели сервера в server_model
            * _main_loop_ основная петля, ядро сервера
            * выделение 2 потоков для чтения данных (команды для сервера и действия игрока)
            * чтение данных с клиентов
            * выделение потока для отправки данных клиенту (реакция сервера)
            * отправка данных клиенту (реакция сервера)
         
    * __server_model.py__ - хранит всю бизнес-логику сервера
        * класс _Server_model_ с методами:
            * выделение id для игрока
            * отключение игрока от сервера
            * подключение игрока к серверу
            * выкинуть игрока в игру
            ###### TODO исправить эти методы ИЛИ -> пойти спать <-
            * отправка клиенту его id на сервере - точнее это перекинется в server(контроллер)
            * обновить время игрока на сервере - тоже должен делать контроллер
            * удалить тех, кто неактивен больше n=15 сек
            * превратить лист таплов в байт строку для отправки клиенту
            * обработка событий от клиента (перемещение) - кто этим должен заниматься ?
            
    * __player.py__ - совокупность всех игроков и методы, которые реализуют их
    действия(перемещения, смерть, СОН, ну может еще СОН) контроллер для player_model
        * класс _Player_ с методами:
            * _init_ инициализация player_model для каждого из игроков, которые появляются
            * перемещения
            * контакт с объектами - думаю это обязаность model
        
    * __player_model.py__ - в идее это основные характеристики игрока, тип его координаты, скин возможно,
    имеющиеся у него пушки, базуки...
        * класс _Player_model_ с методами:
            *
        
    * __game_world.py__ - в моей идее(ну тип мой же проект, я так мыслю)

## SERVER

### Создаем сервер
В методе [*main.py*](./server/main.py) создаем экземпляр класса Server из файла [*server.py*](./server/server.py)
И запускаем метод **main_loop** это основное ядро сервера.

### Основной процесс сервера

Основной процесс сервера идет в методе **main_loop**, который находится в файле [*main.py*](./server/main.py).
Для начала вы все меня заебали
