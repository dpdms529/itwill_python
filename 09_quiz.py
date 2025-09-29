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