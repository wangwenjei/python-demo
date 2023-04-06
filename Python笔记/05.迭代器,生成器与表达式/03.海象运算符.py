"""
    海象运算符是在Python3.8后被提出来的
    由 := 组成
    语法格式为
        variable_name := expression
"""

##################################################################
# if语句
# 传统写法：
# n = 5
# if n > 1:
#     print(f'n <= 5, n is {n}')

# # 海象运算法方式：
# if (n := 5) > 1:
#     print(f'n <= 5, n is {n}')

##################################################################
# while循环
# a = 0
# while a < 5:
#     print(a)
#     a += 1

# # 海象运算法方式：
# a = 0
# while (a := a + 1) < 5:
#     print(a)

##################################################################
# while 循环输入验证

# 常规写法
# user_input = input('input_you_cmd:')
# while user_input != "quit":
#     print('ERR cmd')
#     user_input = input('input_you_cmd:')

# # 海象表达式方式
# while (user_input := input('input_you_cmd:')) != 'quit':
#     print('ERR cmd')

##################################################################
# 常规文件读取  按行读
# with open(r'./test.txt', mode='rt', encoding='utf-8') as f1:
#     while True:
#         line = f1.readline().strip('\n')
#         if not line:
#             break
#         print(line)


# # 海象表达式
# with open(r'./test.txt', mode='rt', encoding='utf-8') as f1:
#     while line := f1.readline().strip('\n'):
#         print(line)

##################################################################
# 推导式
nums = [18, 29, 31, 37, 41, 59, 61, 73, 79, 83, 97]
cnt = 0


# # 传统写法
# def f(x):
#     global cnt
#     cnt += 1
#     return int(x ** 0.5)
#
#
# print([f(x) for x in nums if f(x) > 7])  # ==> [8, 8, 9, 9]
# print(cnt)  #==> 15


# 海象表达式
def f(x):
    global cnt
    cnt += 1
    return int(x ** 0.5)


print([y for x in nums if (y := f(x)) > 7])  # ==> [8, 8, 9, 9]
print(cnt)  # ==> 11  可以看出，在上面那种情况下，使用海象运算符可以减少函数的调用次数
