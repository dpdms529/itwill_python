# 사용자 정의 함수
# 함수, function, method
# test -> 변수
# test() -> 함수

# 함수 선언 형식 : def 함수이름():

data = [1, 4, 5, 7, 2]
print(data)

k = sorted(data)  # 내장함수
print(k)  # [1, 2, 4, 5, 7]

"""
    함수의 정의
    -> 자주 사용하는 명령어들을 그룹화하여 코드를 재사용하는 기법
    -> 함수를 정의하는 것 만으로는 아무런 동작도 하지 않는다
    -> 1) 매개변수(parameter)가 없는 경우
    -> 2) 매개변수가 있는 경우
    -> 3) 리턴(return)값이 있는 경우
    -> 전달값(argument value)
"""


# 1) 매개변수가 없는 경우
def say_hello():
    print("Hello Python")
    print("안녕 파이썬")


# 함수 호출 -> 정의한 함수는 호출되어야만 실행된다
say_hello()
"""
    Hello Python
    안녕 파이썬
"""

# 2) 매개변수가 있는 경우
# 매개변수를 갖는 함수 정의
# -> 함수가 실행되는데 필요한 조건값
# -> 필요한 조건값을 함수이름 옆의 괄호 안에 명시


def test1(x):  # x는 매개변수
    # print(x)
    y = x + 1
    style = "test1({0}) => {0} + 1 = {1}"
    print(style.format(x, y))


test1(3)  # 3 -> 전달값(argument value)
test1(5)
test1(7)

## 매개변수가 2개 이상인 경우
## -> 여러개의 파라미터를 갖는 함수 정의
## -> 파라미터는 필요한 만큼 콤마로 구분하여 정의할 수 있다
## -> 다른 함수의 이름이 중복되지 않도록 주의


def test2(x, y):
    z = x + y
    style = "test2({0}) => {0} + {1} = {2}"
    print(style.format(x, y, z))


test2(1, 3)
test2(2, 4)
test2(5, 6)


## 매개변수에 초기값 설정하기
# def test4(x, y = 0, z):   # 에러 뒤에서부터 설정 가능함
def test3(x, y, z=0):
    style = "test3({0} + {1} + {2}) => {0} + {1} + {2} = {3}"
    print(style.format(x, y, z, x + y + z))


test3(2, 4, 6)  # test3(2 + 4 + 6) => 2 + 4 + 6 = 12
test3(7, 8)  # test3(7 + 8 + 0) => 7 + 8 + 0 = 15
test3(z=30, y=20, x=10)  # test3(10 + 20 + 30) => 10 + 20 + 30 = 60
test3(y=100, x=300)  # test3(300 + 100 + 0) => 300 + 100 + 0 = 400

# 3) 리턴값 있는 경우
# -> 형식) return


def plus(x, y):
    z = x + y
    return z


res = plus(1, 3)
print(res)  # 4

res = plus(2, 4)
print(res)  # 6

# 값, value -> 상수값, 변수값, 함수의 리턴값
# 리턴값을 갖는 함수는 그 결과를 직접 출력하거나 다른 연산에 활용할 수 있다
print(4)  # 4
b = 6
print(b)  # 6
print(plus(5, 6))  # 11
print(abs(-3) + plus(10, 20))  # 33


# return 문을 중간에 만나는 경우 그 즉시 호출시점으로 되돌아 간다
def test4(x, y):
    if x < 10 or y < 10:
        return 0
    z = x + y
    return z


print(test4(100, 200))  # 300
print(test4(5, 15))  # 0
#################################################################


# 문제1) ★기호 100번 출력하기
def graph(c, n):
    print(c * n)


graph("★", 100)


# 문제2) 해당 년도가 윤년 확인하는 함수
def leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if leap(2025):
    print("윤년")
else:
    print("평년")


# 문제3) 팩토리얼값 구하기 4*3*2*1
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


res = fact(4)
print(res)


# 문제4) 두 수사이의 차이를 구하는 함수 (절대값)
def diff(a, b):
    return abs(a - b)


res = diff(7, -4)
print(res)
