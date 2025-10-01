# 1. Scope 유효범위
"""
지역(local)변수와 전역(global)변수
- 함수 안에서 선언되는 변수와 밖에서 선언되는 변수의 범위
"""


def test5():
    c = 1 + 3
    print(c)  # 4


# print(c)    # NameError: name 'c' is not defined
test5()


def test6():
    a = 1
    print(a)  # 1
    # print(b)    # NameError: name 'b' is not defined


test6()


def test7():
    a = 3
    b = 5
    print(a)  # 3


test7()
##################################################################

# 2. 전역변수
x = 100


def exam1():
    print("exam1() : %d" % x)  # 100


def exam2():
    x = 200
    print("exam2() : %d" % x)  # 200 지역 변수의 우선순위가 더 높다


def exam3():
    # 함수나 클래스 안에서 global로 선언하면
    # 밖에서 선언된 변수를 함수나 클래스 안에서 가공이 가능한 형태로 바뀐다
    global x

    x = 300
    print("exam3() : %d" % x)


print(x)  # 100
exam1()  # 100
exam2()  # 200
exam3()  # 300

print(x)  # 300
exam1()  # 300
exam2()  # 200
##################################################################


# 3. 재귀함수
# -> 자신의 함수를 호출


def fact(f):
    if f == 0:
        return 1
    else:
        return f * fact(f - 1)


print(fact(3))  # 6
##################################################################

# 4. callback 함수
# -> 함수를 args 파라미터로 설정해서 사용
# -> 함수가 다른 함수를 호출하여 결과값을 실행
# -> 재귀함수에서 잘 사용


def hap(a, b):
    return a + b


def gop(a, b):
    return a * b


def calc(fn, a, b):
    return fn(a, b)


print(calc(hap, 3, 5))  # 8
print(calc(gop, 4, 6))  # 24
##################################################################

# 5. lambda 함수
# -> 파라미터를 간단한 계산으로 리턴
# -> 메모리를 적게 사용하고 소멸한다
# -> 형식) lambda 파라미터 : 출력할 연산(return 값)

print(hap(2, 4))  # 6

sum = lambda a, b: a + b
print(sum(3, 5))  # 8
