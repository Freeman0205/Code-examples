import time
import random


class Queue:
    def __init__(self):
        self.items = []               # создает очередь

    def is_empty(self):
        return self.items == []       # Проверяет пустая ли очередь

    def enqueue(self, item):
        self.items.insert(0, item)    # Добавляет элементы в очередь

    def dequeue(self):
        return self.items.pop()        # Удаляет элемент из очереди

    def size(self):
        return len(self.items)          # Возвращает количество элементов в очереди


    def simulate_line(self,till_show,max_time):             # Функция моделирующая продажу билетов людям в очереди
                                                          # till_show - целое число, число секунд, оставшихся до начала фильма
                                                           # max_time - целое число, макс. время в секундах на покупку одного билета
        pq = Queue()
        tix_sold = []

        for i in range(100):
            pq.enqueue("кинофанат " + str(i))               # Заполняем очередь людьми покупающими билеты в кино


        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():   # Итерация будет происходить пока время продаж билетов не закончилось или очередь не стала пустой
            now = time.time()
            r = random.randint(0, max_time)        # Длительность времени продажи билета выбранное случайным образом
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)                # Заполнение списка купивших билеты

        return tix_sold

queue = Queue()
sold = queue.simulate_line(30, 3)
print(sold)
