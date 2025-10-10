## 1)
NAME = "Hello Python"


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


## 2)
class Member:
    uname = None
    email = None

    def __init__(self, uname, email):
        print("Member 클래스 생성자 호출됨...")
        self.uname = uname
        self.email = email

    def disp(self):
        style = "이름 : {0} / 이메일 : {1}"
        print(style.format(self.uname, self.email))
