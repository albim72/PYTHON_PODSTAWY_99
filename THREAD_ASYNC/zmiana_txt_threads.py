from time import perf_counter
from threading import Thread

#przeciążenie funkcji
def replace(filename,substr,new_substr):
    print(f'procesowanie pliku: {filename}')
    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()

    content = content.replace(substr,new_substr)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)

def main():

    filenames = [
        'c:/Temp/archiwum/test1.txt',
        'c:/Temp/archiwum/test2.txt',
        'c:/Temp/archiwum/test3.txt',
        'c:/Temp/archiwum/test4.txt',
        'c:/Temp/archiwum/test5.txt',
        'c:/Temp/archiwum/test6.txt',
        'c:/Temp/archiwum/test7.txt',
        'c:/Temp/archiwum/test8.txt',
        'c:/Temp/archiwum/test9.txt',
        'c:/Temp/archiwum/test10.txt',
    ]

    threads = [Thread(target=replace, args=(filename,'id procesu -> ','ids')) for filename in filenames]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f"czas wykonania procesów w wielu wątkach wynosi: {end_time - start_time:0.5f} s")
