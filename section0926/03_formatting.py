print("SEOUL")
print("\n")     # 줄바꿈
print("JEJU")
print("\n\n\n")
print("@\t@")   # 탭 @      @
print("\\")     # /
print("\"")     # "
print("\'")     # '
print('""')     # ""
print("''")     # ''
################################################

print("-" * 30)
"""
    %d 정수
    %f 실수
    %s 문자열
"""

print("나이 : %d" % 25)
print("키 : %f" % 178.9)
print("이름 : %s" % "손흥민")

print("%d년 %d월 %d일" % (2025, 9, 26))
print("%d년\n\n%d월\n%d일" % (2025, 9, 26))
################################################

print("-" * 30)

print("@%d@" % 123)     # @123@
print("@%5d@" % 123)    # @  123@
print("@%-5d@" % 123)   # @123  @    
print("@%05d@" % 123)   # @00123@

money = 123.456789
print("@%f@" % money)       # @123.456789@
print("@%10.3f@" % money)   # @   123.457@
print("@%-10.3f@" % money)  # @123.457   @
print("@%.3f@" % money)     # @123.457   @

print("@%s@" % "KOREA")     # @KOREA@
print("@%10s@" % "KOREA")   # @     KOREA@
print("@%-10s@" % "KOREA")  # @KOREA     @
################################################

print("-" * 30)

name = "손흥민"
kor = 80
eng = 85
mat = 100

total = kor + eng + mat
avg = total / 3

print("이름 : %s" % name)       # 이름 : 손흥민
print("국어 : %d" % kor)        # 국어 : 80
print("영어 : %d" % eng)        # 영어 : 85
print("수학 : %d" % mat)        # 수학 : 100
print("총점 : %d" % total)      # 총점 : 265
print("평균 : %.2f" % avg)      # 평균 : 88.33
################################################

print("-" * 30)

# 출력서식을 재활용할 수 있다
str = "%s 날짜는 %d년 %d월 %d일 입니다"
msg1 = str % ("정모", 2025, 9, 26)
print(msg1) # 정모 날짜는 2025년 9월 26일 입니다

msg2 = str % ("번개", 2025, 10, 26)
print(msg2) # 번개 날짜는 2025년 10월 26일 입니다
################################################

print("-" * 30)

# format() 함수
msg1 = "I eat {0} apples"
print(msg1.format(3))   # I eat 3 apples

msg2 = "{0}은 {1}년 {2}월 {3}일 입니다"
print(msg2.format("크리스마스", 2025, 12, 25))  # 크리스마스은 2025년 12월 25일 입니다

msg3 = "{}은 {}년 {}월 {}일 입니다"
print(msg3.format("추석", 2025, 10, 6))  # 추석은 2025년 10월 6일 입니다

msg4 = "{name}은 {yy}년 {mm}월 {dd}일 입니다"
print(msg4.format(name="크리스마스", yy=2025, mm=12, dd=25))    # 크리스마스은 2025년 12월 25일 입니다

msg5 = "{0}은 {1}년 {mm}월 {dd}일 입니다"
print(msg5.format("한글날", 2025, mm = 10, dd = 9)) # 한글날은 2025년 10월 9일 입니다