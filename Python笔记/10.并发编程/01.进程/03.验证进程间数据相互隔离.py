from multiprocessing import Process

a = 999


def task():
    global a
    a = 100
    print('子: a = %s' % a)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print('主: a = %s' % a)

"""  ==> 
子: a = 100
主: a = 999
"""