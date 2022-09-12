from time import sleep, perf_counter
from threading import Thread

def task(id):
    print(f'start zadania nr {id}')
    sleep(5)
    print(f'zakończone działanie zadania nr {id}')

start_time = perf_counter()

threads = []

for n in range(1,11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()

print(f'wykonanie zadań w 10 wątkach zajęło: {end_time-start_time:0.2f} s')
