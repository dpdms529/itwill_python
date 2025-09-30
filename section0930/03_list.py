"""
    ● [컬렉션]
    - 연속형 자료형
    - 하나의 변수에 여러개의 값을 저장하는 형태
    - List, Tuple, Dictionary, Set, DataFrame, Series
    - Element, 요소, 원소
    - Index, 색인, 순서 (대부분 0부터 시작해서 1씩 증가한다)
    - DataFrame + Series 은 pandas 모듈 설치해야 함
    명령프롬프트 >pip install pandas
"""

# 1. List
## 1) 1차원 리스트
grade = [90, 85, 73, 64, 100]
print(grade)        # [90, 85, 73, 64, 100]
print(type(grade))  # <class 'list'>

print(grade[0])
print(grade[1])
print(grade[2])
print(grade[3])
print(grade[4])

print(len(grade)) # 5 요소의 개수

for idx in range(len(grade)):
    print(grade[idx])

names = ["홍길동", "무궁화", "개나리", "진달래", "라일락"]
print(names)
print(type(names))

for name in names:
    print(name)

num = [5, 8, -1, 9, -6]
size = len(num)

# 문제 1) 음수의 개수를 구하시요
cntNegative = 0

for n in num:
    if n < 0:
        cntNegative += 1

print(cntNegative)

# 문제 2) 양수 중에서 홀수의 합을 구하시오
sumOfOdd = 0

for n in num:
    if n > 0 and n % 2 == 1:
        sumOfOdd += n

print(sumOfOdd)

# 문제 3) num[4]의 등수를 구하시오
rank = 1

target = num[4]

for n in num:
    if target < n:
        rank += 1

print(f'{target} : {rank}등')
########################################################

## 2) 2차원 리스트
## -> 행(row)과 열(col)로 구성
students = [
    ["joy", 20],
    ["kiara", 30],
    ["tom", 40],
]   # 3행 2열

print(students)         # [['joy', 20], ['kiara', 30], ['tom', 40]]
print(type(students))   # <class 'list'>

# 행 전체
print(students[0])          # ['joy', 20]
print(students[1])          # ['kiara', 30]
print(students[2])          # ['tom', 40]

# 각 요소 값 [행][열]
print(students[0][0])       # joy
print(students[0][1])       # 20

for y in students:
    for x in y:
        print(x)

print(len(students))        # 3 -> 행의 개수
print(len(students[0]))     # 2 -> 0행의 열의 개수
print(len(students[1]))     # 2 -> 1행의 열의 개수
print(len(students[2]))     # 2 -> 2행의 열의 개수

row = len(students)         # 3
for r in range(row):        # 0~2
    col = len(students[r])
    for c in range(col):
        print(students[r][c])

# print(students[3][3])   # 에러 IndexError: list index out of range
# 3행 3열은 존재하지 않음
######################################################################

## 3) 리스트 관련 함수
## -> 리스트의 인덱싱, 슬라이싱

mylist = [10, 20, 30, 40, 50]

for m in mylist:    # for 요소값 in 덩어리
    print(m)

print(mylist[1:3])      # [20, 30]
print(mylist[1:-2])     # [20, 30]

mylist.append(60)       # 맨뒤 요소 추가    
print(mylist)           # [10, 20, 30, 40, 50, 60]

mylist.insert(1, 30)    # 1번째 요소로 30 삽입
print(mylist)           # [10, 30, 20, 30, 40, 50, 60]

print(mylist.count(30)) # 2 30값의 개수

mylist.pop()            # 마지막 요소 삭제
print(mylist)           # [10, 30, 20, 30, 40, 50]

x = mylist.index(30)
print(x)                # 1

mylist.remove(30)  
print(mylist)           # [10, 20, 30, 40, 50]

score = [9, 3, 5, 1, 7]

score.reverse() # 순서 뒤집기
print(score)    # [7, 1, 5, 3, 9]

score.sort()    # 오름차순 정렬 Ascending Sort (1->9, A->Z, a->z, ㄱ->ㅎ)
print(score)    # [1, 3, 5, 7, 9]

score.sort(reverse=True)    # 내림차순 정렬 Descending Sort
print(score)                # [9, 7, 5, 3, 1]

str = "Gone,With,The,Wind"
word = str.split(',')
print(word)         # ['Gone', 'With', 'The', 'Wind']
print(type(word))   # <class 'list'>

for w in word:
    print(w)