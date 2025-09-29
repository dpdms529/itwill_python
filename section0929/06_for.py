# 반복문 : forans, while문
# break문, continue문
# 무한 Loop => 끝이 없는 반복

"""
    for 변수 in range(시작값, 종료값-1, 증감) : 
        반복할 처리식
"""

# a는 0 ~ 4까지 5번 반복
for a in range(5):
    print(a)
    print("Python")

# b는 1 ~ 4까지 4번 반복
for b in range(1, 5):
    print(b)
    print("ITWILL")

# c는 1부터 4까지 2씩 증가
for c in range(1, 5, 2):
    print(c)
    print("KOREA")

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()
