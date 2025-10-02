# 생성자와 소멸자

# 1. 생성자 함수 Constructor
# ->생성자 함수는 클래스를 이용해서 객체를 생성할 때 사용한다
# ->클래스명과 동일한 함수이름으로 호출한다


## 1) 매개변수가 없는 생성자 함수
class Member:
    uname = None
    email = None

    # 생성자 함수. init 앞뒤로 언더라인 2개
    # 객체 생성할 때 Member()라는 이름으로 호출된다
    # 기본생성자 함수 default constructor
    def __init__(self):
        # pass 함수 안에 아무 내용도 없을 때
        print("Member() 생성자 함수 호출됨")
        self.uname = "손흥민"
        self.email = "son@itwill.com"

    def disp(self):
        print(f"이름: {self.uname} / 이메일: {self.email}")


mem1 = Member()  # Member() 생성자 함수 호출됨
mem1.disp()  # 이름: 손흥민 / 이메일: son@itwill.com

mem2 = Member()
mem2.disp()


## 2) 매개변수가 있는 생성자 함수
class User:
    uname = None
    email = None

    def __init__(self, uname, email):
        print("매개변수가 있는 User() 생성자 함수 호출됨")
        self.uname = uname
        self.email = email

    def disp(self):
        print(f"이름: {self.uname} / 이메일: {self.email}")


user1 = User("김연아", "kim@itwill.com")  # 매개변수가 있는 User() 생성자 함수 호출됨
user1.disp()  # 이름: 김연아 / 이메일: kim@itwill.com

user2 = User("박지성", "park@itwill.com")
user2.disp()


# 2. 소멸자 Destructor
# -> 메모리에서 객체를 소멸할 때 자동으로 호출되는 함수
class Student:
    uname = None
    email = None

    def __init__(self, uname, email):
        print("매개변수가 있는 Student() 생성자 함수 호출됨")
        self.uname = uname
        self.email = email

    def disp(self):
        print(f"이름: {self.uname} / 이메일: {self.email}")

    def __del__(self):
        print("소멸자 함수 호출됨...")


stu1 = Student("라일락", "ra@itwill.com")
stu1.disp()

stu2 = Student("무궁화", "mu@itwill.com")
del stu2  # stu2 객체 강제 삭제
# stu2.disp()  # NameError: name 'stu2' is not defined.
