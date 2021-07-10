import subprocess

obj = subprocess.Popen('echo 123;ls /root11',  # 执行的系统命令
                       shell=True,
                       stdout=subprocess.PIPE,  # 将正确的结果信息 通过管道发送给stdout
                       stderr=subprocess.PIPE   # 将错误的结果信息 通过管道发送给stderr
)

res = obj.stdout.read()
res_err = obj.stderr.read()

print(res.decode('utf-8'),end='')  # ===> 123
print(res_err.decode('utf-8'))     # ===> ls: /root11: No such file or directory

