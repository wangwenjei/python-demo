from threading import Thread

a = 999


def task():
    global a
    a = 666
    print('线 %s' % a)


if __name__ == '__main__':
    t = Thread(target=task)
    t.start()
    t.join()
    print('主 %s' % a)

""" ===>> 
线 666
主 666
"""