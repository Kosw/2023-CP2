from threading import Thread
import time

def func0():
    list_var = [1, 2, 3]
    for x in list_var:
        print(x)
        time.sleep(1)

def func1():
    list_var = ['a', 'b', 'c']
    for x in list_var:
        print(x)
        time.sleep(0.5)

if __name__ == '__main__':
    p0 = Thread(target=func0())
    p1 = Thread(target=func1())
    p0.start()
    p1.start()
    print("threading is done.")