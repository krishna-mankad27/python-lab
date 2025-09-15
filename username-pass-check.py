username = "kadi@4318"
password = "hello6187"
cnt = 0
while cnt < 3 :
    x = input("enter username : ")
    if x == username:
        cnt +=1
        y = input("enter password : ")
        if y == password:
            print("access granted")
            break
        else:
            print("access denied\nattempts remaining",3-cnt)
    else:
        print("invalid username ")