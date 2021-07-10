print("模块m=====>")
x = 1
__all__ = ['x','get']
def get():
    print(x)

def change():
    global x
    x = 0


if __name__ == '__main__':
    change()
