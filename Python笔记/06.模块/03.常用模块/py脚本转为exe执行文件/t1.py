import os

# file = os.getcwd()
# if not os.path.exists(file + 'test.txt'):
#     os.mknod("test.txt")
#

with open(r'test.txt', mode='wt', encoding='utf-8') as f:
    f.write('hello world!!!')
