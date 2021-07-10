import random




def make_code(size: int = 4) -> str:
    # 打印随机字符串
    res = ''
    for i in range(size):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0, 9))
        res += random.choice([s1, s2])
    return res
print(make_code(6))
