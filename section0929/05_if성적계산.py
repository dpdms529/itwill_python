# 성적 프로그램
name = "손흥민"
kor = 100
eng = 100
mat = 35
avg = (kor + eng + mat) // 3

print(f"이름: {name}")
print(f"국어: {kor}")
print(f"영어: {eng}")
print(f"수학: {mat}")
print(f"평균: {avg}")

#문제1) 평균이 95점 이상이면 장학생 출력
if avg >= 95:
    print("장학생")

#문제2) 국어점수가 70점 이상이면 국어:합격 아니면 국어:불합격
if kor >= 70:
    print("국어: 합격")
else:
    print("국어: 불합격")

#문제3) 수학점수 90점 이상이면 수학:A학점
#              80점 이상이면 수학:B학점
#              70점 이상이면 수학:C학점
#              60점 이상이면 수학:D학점
#              아니면 수학:F학점
if mat >= 90:
    print("수학: A학점")
elif mat >= 80:
    print("수학: B학점")
elif mat >= 70:
    print("수학: C학점")
elif mat >= 60:
    print("수학: D학점")
else:
    print("수학: F학점")

#문제4) 과락
#       평균이 70점이상이면 결과:합격
#       (단, 국영수 세과목 중에서 한과목이라도 40점미만이면 결과:재시험)
#       평균이 70점미만이면 결과:불합격
if avg >= 70:
    if kor >= 40 and eng >= 40 and mat >= 40:
        print("결과: 합격")
    else:
        print("결과: 재시험")
else:
    print("결과: 불합격")

"""
    결과
    이름: 손흥민
    국어: 100
    영어: 100
    수학: 35
    평균: 78
    국어: 합격
    수학: F학점
    결과: 재시험
"""