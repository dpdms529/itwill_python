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