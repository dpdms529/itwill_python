# 2. Tuple
# 리스트와 기본적으로 동일하지만, 처음 할당한 요소의 값을 수정할 수 없다

grade = (12, 13, 14, 15, 16)
print(grade)    # (12, 13, 14, 15, 16)
print(grade[0]) # 12
# print(grade(0)) # 에러 TypeError: 'tuple' object is not callable

names = ("홍길동", "무궁화", "진달래", "개나리", "라일락")
print(names)

stud1 = ("봉선화", 90)
print(stud1)        # ('봉선화', 90)
print(stud1[0])     # 봉선화
print(stud1[1])     # 90

# stud1[0] = "코리아" # 에러 TypeError: 'tuple' object does not support item assignment