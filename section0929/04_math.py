# math 함수 : 수학 관련
# 모듈 : 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것
# 패키지 : 모듈들을 모은 컬렉션

## 1) import 하지 않고 사용할 수 있는 내장 함수
x = min(1, 2, 3, 4, 5)  # 최소값
y = max(1, 2, 3, 4, 5)  # 최대값
print(x)    # 1
print(y)    # 5

x = abs(3)  # 절대값
y = abs(-3)
print(x)    # 3
print(y)    # 3

x = pow(2, 4)   # 2의 4승
print(x)    # 16

# round는 소수점을 반올림한 값을 리턴
print(round(123.456, 2))    # 123.46
print(round(123.453, 2))    # 123.45

## 2) math 모듈
import math # 모듈 선언

print(math.pi)  # 3.141592653589793

# 소수점 올림
x = math.ceil(2.2)  # 3
y = math.ceil(3.5)  # 4
print(x)
print(y)

# 소수점 버림
x = math.floor(2.2) # 2
y = math.floor(3.5) # 3
print(x)
print(y)

from math import ceil, floor

# math 모듈명 생략 가능
print(ceil(2.1))
print(floor(2.1))