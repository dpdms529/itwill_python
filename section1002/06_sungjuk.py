# numpy 모듈 연습
# 5명의 학생들 대상으로 총점, 평균, 등수 구하기
"""
출력 결과
이름   국어  영어  수학  총점  평균  등수
손흥민  100  100  100    0     0    1
박지성   85   85   55    0     0    1
김연아   30   40   66    0     0    1
개나리  100   35   95    0     0    1
진달래   95   80   70    0     0    1
"""

import numpy as np

# 성적 프로그램 완성하기
name = ["손흥민", "박지성", "김연아", "개나리", "진달래"]  # 1차원 리스트
kor = np.array([100, 85, 30, 100, 95])  # list를 배열로 변환
eng = np.array([100, 85, 40, 35, 80])
mat = np.array([100, 55, 66, 95, 70])

size = len(name)
# 문제1) 총점 구하기
total = kor + eng + mat
print(total)

# 문제2) 평균구하기
avg = total / 3
print(avg)

# 문제3) 평균을 기준으로 모든 요소의 등수를 구하시오
rank = np.ones(size, dtype="int")

for i in range(size):
    for j in range(size):
        if avg[i] < avg[j]:
            rank[i] += 1

print(rank)

# 출력하기
for i in range(size):
    # 문제4) 과락 (평균을 기준으로 재시험, 합격, 불합격)
    result = ""
    if avg[i] > 60:
        if kor[i] >= 40 and eng[i] >= 40 and mat[i] >= 40:
            result = "합격"
        else:
            result = "재시험"
    else:
        result = "불합격"

    # 문제5) 평균 10점당 * 한개씩
    star = "★" * int(avg[i] // 10)

    # 문제6) 평균 95점이상 장학생 출력
    scholar = "장학생" if avg[i] >= 95 else ""

    print(
        "%-8s %5d %5d %5d %5d %5d %5d %-10s %-5s %-5s"
        % (
            name[i],
            kor[i],
            eng[i],
            mat[i],
            total[i],
            avg[i],
            rank[i],
            star,
            result,
            scholar,
        )
    )
