
from day12.atm.user import User
from day12.atm.card import Card
import random
import pickle


class ATM:

    userDict={}
    islogin = None

    @staticmethod
    def welcome():
        print('''
           **********************
           *                    *
           *  welcome to bank   *
           *                    *
           **********************
           ''')

    @staticmethod
    def select():
        print('''
           **********************
           *  1.登陆   2.开户    *
           *  3.查询   4.取款    *
           *  5.存款   0.退出    *
           *  6.转账   7.改密    *
           *  8.锁卡   9.解锁    *
           **********************
           ''')
        num = input("请选择服务项目：")
        return num

    @classmethod
    def getcardnum(cls):
        cardnum = ""
        for x in range(6):
            cardnum += str(random.randrange(0,10))
        try:
            with open("user.txt", "rb") as f:
                cls.userDict = pickle.load(f)
        except:
            pass
        if cardnum not in cls.userDict:
            return cardnum

    @classmethod
    def openUser(cls):
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号码：")
        phonenum = input("请输入您的电话号码：")
        psd = input("请设置您的密码：")
        psd2 = input("请确认您的密码：")
        if psd == psd2:
            mon = int(input("请输入您的预存余额："))
            if mon>0:
                cardnum = cls.getcardnum()
                card = Card(cardnum,psd,mon)
                user = User(name,idcard,phonenum,card)
                cls.userDict[cardnum] = user
                print("开卡成功，您的卡号为%s,请牢记..."%cardnum)


            else:
                print("预存余额非法，开卡失败...")

        else:
            print("两次输入密码不一致，开卡失败...")


    @classmethod
    def login(cls):
        if cls.islogin != "false":
            cardnum = input("请输入您的卡号：")
            user = cls.userDict.get(cardnum)
            if user:
                for i in range(3):
                    psd = input("请输入您的密码:")
                    if psd != user.card.password:
                        print("密码错误，登录失败。。。")

                    else:
                        print("恭喜你，登录成功！！！")
                        cls.islogin = cardnum
                        break
                else:
                    cls.islogin = "false"
                    cls.num = cardnum
                    print("你的账号已锁定,请解锁")

            else:
                print("卡号不存在，请查证后登录。。。")
        else:
            print("你的账号已被锁定")



    @classmethod
    def search(cls):
        if cls.islogin != "false" and cls.islogin:
            print("您当前的余额为%d"%(cls.userDict.get(cls.islogin).card.money))

        else:
            print("请登录后查询")

    @classmethod
    def dmoney(cls):
        if cls.islogin != "false" and cls.islogin:
            print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
            i = int(input("请输入取款金额:"))
            if cls.userDict.get(cls.islogin).card.money - i < 0:
                print("余额不足,无法操作")
            else:
                cls.userDict.get(cls.islogin).card.money -= i
                print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
        else:
            print("请登录后取款")


    @classmethod
    def gmoney(cls):
        if cls.islogin != "false" and cls.islogin:
            print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
            i = int(input("请输入存款金额:"))
            cls.userDict.get(cls.islogin).card.money +=i
            print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
        else:
            print("请登录后存款")

    @classmethod
    def zmoney(cls):
        if cls.islogin != "false" and cls.islogin:
            print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
            i = input("请输入对方账号")
            if i in list(cls.userDict.keys()):
                j = int(input("请输入转账金额:"))
                cls.userDict.get(cls.islogin).card.money -= j
                print("您当前的余额为%d" % (cls.userDict.get(cls.islogin).card.money))
            else:
                print("你输入的账号不存在")
        else:
            print("请登录后转账")

    @classmethod
    def spassword(cls):
        if cls.islogin != "false" and cls.islogin:
            while True:
                i = input("请输入你的旧密码")
                if i == cls.userDict.get(cls.islogin).card.password:
                    s = input("请输入你的新密码")
                    cls.userDict.get(cls.islogin).card.password = s
                    print("密码修改成功")
                    break
                else:
                    print("你输入的旧密码错误,请重新输入")

        else:
            print("请登录后改密")

    @classmethod
    def cleanlook(cls):
        if cls.islogin == "false" and cls.islogin:
            i = input("请输入身份证号码:")
            if i == cls.userDict.get(cls.num).idcard:
                cls.islogin = cls.num
                s = input("请输入新密码:")
                cls.userDict.get(cls.islogin).card.password = s
        else:
            print("当前状态,无法解锁")

