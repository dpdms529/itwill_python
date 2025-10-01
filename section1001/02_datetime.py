#  시스템의 현재 날짜 정보 조회하기

import datetime as dt

# 현재 날짜(년월일시분초) 정보 가져오기
today = dt.datetime.now()
print(today)  # 2025-10-01 11:48:07.155920
print(today.year)  # 2025
print(today.month)  # 10
print(today.day)  # 1
print(today.hour)  # 11
print(today.minute)  # 48
print(today.second)  # 07
print(today.microsecond)  # 155920

# 요일 반환 0(월) 1(화) 2(수) 3(목) 4(금) 5(토) 6(일)
print(today.weekday())  # 2 -> 수요일


# 요일 이름 출력
days = ("월", "화", "수", "목", "금", "토", "일")  # 튜플
print(days[today.weekday()])

# 출력 형식 만들기
print(today.strftime("%y/%m/%d %H:%M:%S"))  # 25/10/01 11:59:16
print(today.strftime("%Y/%m/%d %H:%M:%S %a %A %p"))
# 2025/10/01 11:59:16 Wed Wednesday AM
