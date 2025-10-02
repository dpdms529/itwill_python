# numpy 모듈 기반 배열 연산

ls1 = [82, 76, 91, 65]

# 문제) ls1 각 요소에 2씩 더하기
# -> [84, 78, 93, 67]

ls2 = []
for idx in range(4):
    ls2.append(ls1[idx] + 2)

print(ls2)  # [84, 78, 93, 67]

# 문제) 인덱스가 동일한 각 요소끼리 더해서 ls5에 저장
ls3 = [10, 15, 20, 25, 30]
ls4 = [2, 3, 4, 5, 6]
ls5 = [0, 0, 0, 0, 0]

i = 0
for idx in range(5):
    ls5[idx] = ls3[idx] + ls4[idx]

print(ls5)  # [12, 18, 24, 30, 36]
#################################################################

import numpy as np

grade = np.array([82, 76, 91, 65])
print(grade)

# new1 = ls1 + 2 -> 에러

new1 = grade + 2  # 각 요소에 2씩 더함
print(grade)  # [84, 78, 93, 67]

new2 = grade - 5  # 각 요소에 5씩 뺌
print(new2)  # [77 71 86 60]

arr1 = np.array([10, 15, 20, 25, 30])
arr2 = np.array([2, 3, 4, 5, 6])

arr3 = arr1 + arr2  # 인덱스가 동일한 요소끼리 더하기
print(arr3)  # [12, 18, 24, 30, 36]

arr4 = arr2 - arr1
print(arr4)  # [ -8 -12 -16 -20 -24]

# 집계함수
aver = np.array([82, 76, 91, 65])
print("총점 : %d" % np.sum(aver))  # 314
print("평균 : %d" % np.average(aver))  # 78
print("최대값 : %d" % np.max(aver))  # 91
print("최소값 : %d" % np.min(aver))  # 65
#################################################################

# numpy 모듈을 활용한 정형화된 배열 만들기
a = np.arange(15)
print(a)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

b = np.arange(100, 115)
print(b)  # [100 101 102 103 104 105 106 107 108 109 110 111 112 113 114]
print(len(b))  # 15

# 모든 요소가 실수형
c = np.zeros(3)
print(c)  # [0. 0. 0.]

d = np.zeros(4, dtype="int")
print(d)  # [0 0 0 0]

e = np.ones(3)
print(e)  # [1. 1. 1.]

f = np.ones(4, dtype="int")
print(f)  # [1 1 1 1]

g = np.full(5, 7)
print(g)  # [7 7 7 7 7]

h = np.full(4, 7, dtype="float")
print(h)  # [7. 7. 7. 7.]
