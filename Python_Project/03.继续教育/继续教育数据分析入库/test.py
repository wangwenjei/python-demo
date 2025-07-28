a = ['a', 'b', 'c', 'd']

# for i in a:
#     print(i)

b = ["ID:" + i for i in a]
print(b)

c = {"id" + str(idx): i for idx, i in enumerate(a)}
print(c)

x = 20
y = 30

max_value = x if x > y else y
print(max_value)  # 输出: 20

print(x) if x > y else print(y)
