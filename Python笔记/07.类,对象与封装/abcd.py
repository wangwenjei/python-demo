class Email(object):
    def __init__(self):
        self.target = '123@163.com'
        self.my = '2254964433@qq.com'

    def send(self, content):
        print('%s 给 %s 发送了: %s' % (self.my, self.target, content))


obj = Email()

# obj.send('hello')
