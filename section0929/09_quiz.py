# 문제1) 1 ~ 3 사이의 합을 구하시오
sum = 0
for i in range(1, 4):
    sum += i
print(sum)  # 6

# 문제2) 4팩토리얼 값을 구하시오(누적의 곱)
fac = 1
for i in range(1, 5):
    fac *= i
print(fac)  # 24

# 문자3) 두 수 사이의 수를 전부 더하시오
a = 10
b = 1
sum = 0

# 만일, 앞의 수가 뒤의 수보다 크면 두 변수의 값을 서로 교환(swap)
"""
    if a > b:
        tmp = a
        a = b
        b = tmp
"""
if a > b:
    a, b = b, a

for i in range(a, b + 1):
    sum += i
print(sum)  # 55

#문제4) 간단한 계산기 프로그램
""" 
    실행화면   
    3 + 5 = 8   
    3 - 5 = -2
    3 * 5 = 15
    3 / 5 = 0.6   
    3 % 5 = 3   
""" 
a = 3
b = 5
op = ["+", "-", "*", "/", "%"]

for o in op:
    if o == "+":
        print(f"{a} {o} {b} = {a + b}")
    elif o == "-":
        print(f"{a} {o} {b} = {a - b}")
    elif o == "*":
        print(f"{a} {o} {b} = {a * b}")
    elif o == "/":
        print(f"{a} {o} {b} = {a / b}")
    elif o == "%":
        print(f"{a} {o} {b} = {a % b}")

#문제5) 1~100중에서 짝수의 합, 홀수의 합을 각각 구하시오
even = 0  #짝수의 합
odd = 0   #홀수의 합

for i in range(1, 101, 2):
    odd += i
    even += i + 1

print(f"짝수의 합: {even}")
print(f"홀수의 합: {odd}")

#문제6) 운행거리에 따라 택시 요금을 계산하는 프로그램
#      2000m까지는 기본요금 900원이고
#      2000m초과 운행시 200m단위마다 기본요금에 100원씩 가산하여 요금을 계산한다
"""
    예1) 운행거리 1600 -> 기본요금 : 900
    예2) 운행거리 3000 -> 1000초과 (기본요금 900 + 추가 500 = 1400)
    예3) 운행거리 2900 ->  900초과 (기본요금 900 + 추가 500 = 1400)
"""
import math

distance = 2900
charge = 900

if distance > 2000:
    diff = distance - 2000
    add = math.ceil(diff / 200) * 100
    charge += add

print(f"택시 요금은 {charge}원입니다")
