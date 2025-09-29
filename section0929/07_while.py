# 반복문
"""
       while 조건:
            조건이 True이면 처리
            조건이 True이면 처리
            조건이 True이면 처리
"""

# 증가에 따른 반복
i = 1
while i <= 3:
    print("Python")
    i = i + 1

# 감소에 따른 반복
j = 3
while j >= 1:
    print("ITWILL")
    j = j - 1

# 구구단
i = 1
j = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i*j}")
        j = j + 1
    i = i + 1
    print()