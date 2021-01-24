# break 和 continue 在Python中只能用于循环语句
# break：用来结束整个循环
# continue：用来结束本轮循环，开启下一轮循环

while True:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'zs' and password == '123':
        break
