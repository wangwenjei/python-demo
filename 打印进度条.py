import time

def progress(perent):
    if perent > 1:
        perent = 1
    res = int(perent*50) * '#'
    print('\r[%-50s] %d%%' % (res,int(perent*100)), end='')

recv_size = 0
total_size = 102512

while recv_size < total_size:
    time.sleep(0.1)
    recv_size += 1024
    perent = recv_size / total_size
    progress(perent)