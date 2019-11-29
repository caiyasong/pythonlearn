#!/usr/bin/python3
#-*- coding: utf-8 -*-
#-*- author:zhangjiao -*-
from day12.atm.atm import ATM
import time
import pickle

if __name__ == '__main__':
    ATM.welcome()
    try:
        with open("user.txt","rb") as f:
            ATM.userDict = pickle.load(f)
    except:
        pass
    while True:
        time.sleep(1)
        print(ATM.userDict)
        num = ATM.select()
        if num == "2":
            print("开户")
            ATM.openUser()
        elif num == "0":
            print("退出")
            with open("user.txt","wb") as f2:
                # print(type(ATM.userDict))
                    pickle.dump(ATM.userDict,f2)
            break
        elif num == "1":
            print("登录")
            ATM.login()
        elif num == "3":
            print("查询")
            ATM.search()
        elif num == "4":
            print("取款")
            ATM.dmoney()
        elif num == "5":
            print("存款")
            ATM.gmoney()
        elif num == "6":
            print("转账")
            ATM.zmoney()
        elif num == "7":
            print("改密")
            ATM.spassword()
        elif num == "9":
            print("解锁")
            ATM.cleanlook()
        else:
            print("选择有误请重新选择...")
