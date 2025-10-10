# 모듈(module)의 활용
# -> 모듈:다른 프로그램에서 활용하기 위한 프로그램 조각, 남이 만들어둔 코드의 집합
# -> 하나의 파이썬 .py 파일이 하나의 모듈이 된다
# -> 모듈 선언 형식) import 파일이름 또는 모듈이름

# 모듈 파일 my_module.py

## 1) 모듈 import
import my_module

print(my_module.NAME)  # Hello Python
print(my_module.plus(1, 3))  # 4
print(my_module.minus(2, 4))  # -2

## 2) 별칭
import my_module as mm

print(mm.NAME)  # Hello Python
print(mm.plus(1, 3))  # 4
print(mm.minus(2, 4))  # -2

## 3) 특정 기능만 가져오기
from my_module import NAME
from my_module import plus

print(NAME)  # Hello Python
print(plus(5, 3))  # 8
# print(minus(5, 3))  # NameError: name 'minus' is not defined
