class Test():
    def peonle(self, name):
        # print('name: %s' % name)
        return 'name: %s' % name

def cat():
    print(111)

def req():
    pass

obj = Test()
res = obj.peonle('jason')
print(res)

if __name__ == '__main__':
    cat()