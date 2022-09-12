from time import sleep, perf_counter
from threading import Thread

def task():
    print('start zadania...')
    sleep(5)
    print('wykonane')

print("sprawdźmy czas pracy w jednym wątku: ")
start_time = perf_counter()

task()
task()
task()

end_time = perf_counter()


print(f'wykonanie zadań zajęło: {end_time-start_time:0.2f} s')


print("sprawdźmy czas pracy w wielu wątkach: ")
start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)
t3 = Thread(target=task)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = perf_counter()
print(f'wykonanie zadań w wielu wątkach zajęło: {end_time-start_time:0.2f} s')
