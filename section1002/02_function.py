# 참조 https://www.w3schools.com/python/python_functions.asp

# 1. Arguments와 Keyword Arguments
# -> Argument 전달값, 보내는 값
# -> Parameter 받는값
# -> 함수 선언시 파라미터의 수를 특정할 수 없을 경우 사용
# -> keyword arguments의 경우 아규먼트로 함수 호출 시 키워드를 작성하여 호출
# -> arguments는 튜플 타입
# -> keyword arguments는 딕셔너리 타입


## 1) Arguments, *args
def test1(fname, lname):
    print(fname + " " + lname)


test1("손", "흥민")  # 손 흥민
# test1("김") TypeError: test1() missing 1 required positional argument: 'lname'


def test2(*names):
    print(names)
    print(type(names))  # 튜플
    print(len(names))
    # 맨 마지막 요소값 출력
    print(names[-1])


test2("개나리", "진달래", "무궁화", "라일락", "코리아")
# ('개나리', '진달래', '무궁화', '라일락', '코리아')
# <class 'tuple'>
# 5
# 코리아


## 2) Keyword Arguments, **Kwargs
def test3(**phones):
    print(phones)
    print(type(phones))  # 딕셔너리
    print(phones["phone3"])


test3(phone1="123", phone2="456", phone3="789")
# {'phone1': '123', 'phone2': '456', 'phone3': '789'}
# <class 'dict'>
# 789


## 3) *args와 **kwargs
def hap(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return sum(args) + sum(kwargs.values())


print(hap(1, 2, 3, 4, num1=5, num2=6))
# <class 'tuple'> (1, 2, 3, 4)
# <class 'dict'> {'num1': 5, 'num2': 6}
# 21


## 4) list 타입 데이터를 args로 호출하는 방법
def gop(n1, n2, n3):
    return n1 * n2 * n3


ls = [2, 3, 4]
print(gop(ls[0], ls[1], ls[2]))  # 24
print(gop(*ls))  # 24

# 주의사항 : list 요소의 갯수와 파라미터의 갯수ㅏㄱ 일치해야 함
ls2 = [2, 3, 4, 5]
# gop(*ls2)   TypeError: gop() takes 3 positional arguments but 4 were given


def hap2(*args):
    return sum(args)


ls3 = [3, 4, 5, 6]
print(hap2(*ls3))  # 18
