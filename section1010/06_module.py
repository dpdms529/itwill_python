# 객체가 정의된 모듈 참조
# 모듈 파일 my_module.py 작성

## 1)
import my_module

print(my_module.mycalc.plus(3, 2))  # 5
print(my_module.mycalc.minus(3, 2))  # 1

## 2) 모듈 자체에 별칭 부여
import my_module as mm

print(mm.mycalc.plus(3, 2))  # 5
print(mm.mycalc.minus(3, 2))  # 1

## 3) 모듈에 정의된 특정 객체만 가져오기
from my_module import mycalc

print(mycalc.plus(3, 2))  # 5
print(mycalc.minus(3, 2))  # 1
