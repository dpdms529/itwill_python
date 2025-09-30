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

# switch 이론
# -> 짝수/홀수, Yes/No, On/Off, True/False
even = 0
odd = 0
flag = False
i = 1

while i <= 100:
    if flag :
        flag = False
        even += i
    else:
        flag = True
        odd += i
    i += 1

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