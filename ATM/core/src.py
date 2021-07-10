def login():
    print('登录功能')

def transfer():
    print('转账功能')

func_dic = {
    '0':['退出',exit],
    '1':['登录',login],
    '2':['转账',transfer]
}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][0])

        user_instruction = input("输入需要执行的指令").strip()

        if not user_instruction.isdigit():
            print('==请输入数字指令==')
            continue

        if user_instruction  in func_dic :
            func_dic[user_instruction][1]()
        else:
            print('==请输入规定的数字指令==')











run()