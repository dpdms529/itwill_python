# break 문
# -> 반복문 안에서 루프를 빠져나오기 위해

a = 1
while a < 10:
    if a == 5: break
    print(a)
    a = a + 1

"""
    1
    2
    3
"""
#################################################

# continue 문
# -> 루프 블럭의 나머지 문장들을 실행하지 않고
# -> 다음 루프로 직접 돌아가게 할 수 있다
b = 1
while b < 10:
    b = b + 1
    if b == 5: continue
    print(b)

"""
    2
    3
    4
    6
    7
    8
    9
    10
"""
#################################################

# 이중 반복문
for a in range(3):
    print("KOREA")
    for b in range(2):
        print("SEOUL")
"""
    KOREA
    SEOUL
    SEOUL
    KOREA
    SEOUL
    SEOUL
    KOREA
    SEOUL
    SEOUL
"""

a = 1
while a <= 2:
    print("Python")
    a = a + 1
    b = 1
    while b <= 3:
        print("JAVA")
        b = b + 1
"""
    Python
    JAVA
    JAVA
    JAVA
    Python
    JAVA
    JAVA
    JAVA
"""