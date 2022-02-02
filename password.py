password = 'a123456'
x = 3
while True:
    pwd = input('請輸入密碼:')
    x = x - 1
    if pwd == password:
        print('密碼正確，成功登入')
        break
    else:
        print('密碼錯誤，您還有', x ,'次機會')
        if x == 0:
            print('輸入錯誤，已被鎖')
            break

