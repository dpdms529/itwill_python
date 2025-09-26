# 연산자
# -> 이식성 풍부하다
# -> 산술, 비교, 논리연산자

# 1. 산술연산자
print(5+3)  # 더하기 8
print(5-3)  # 빼기 2
print(5*3)  # 곱하기 15
print(5/3)  # 나누기 1.6666666666666667
print(5//3) # 몫 1
print(5%3)  # 나머지 2

print(3/5)  # 0.6
print(3//5) # 0
print(3%5)  # 3
print(3**5) # 제곱 243
##########################################################

print("-" * 30)

# 2. 비교 연산자 (관계)
# -> 결과값이 논리형(참, 거짓)으로 반환
# -> 논리형(boolean) : True/False
print(3 < 5)    # 작다 True
print(3 > 5)    # 크다 False
print(3 <= 5)   # 작거나 같다 True
print(3 >= 5)   # 크거나 같다 False
print(3 == 5)   # 같다 False
print(3 != 5)   # 같지 않다 True
##########################################################

print("-" * 30)

# 3. 논리 연산자
# -> 조건이 2개 이상일 때 전체적으로 판단
# -> 결과 값이 논리형(참, 거짓)으로 반환된다
# -> and, or, not

## 1) and 연산자
## -> 그리고, ~이면서
## -> 모든 조건을 만족하면 True
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  #False

## 2) or 연산자
## -> 또는, ~이거나
## -> 조건들 중에서 하나라도 True이면 True
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

## 3) not 연산자
## -> 부정 연산자, ~아니라면
flag = not(3 < 5)
print(flag) # False
##########################################################

print("-" * 30)

# 4) 할당 연산자
a = 1       # a = 1
a = a + 3   # a = 4
a += 3      # a = 7
print(a)

b = 3       # b = 3
b = b - 1   # b = 2
b -= 1      # b = 1
print(b)

c = 5       # c = 5
c = c * 2   # c = 10
c *= 2      # c = 20
print(c)

d = 7       # d = 7
d = d / 3   # d = 2.3333333333333335
d /= 3      # d = 0.7777777777777778
print(d)