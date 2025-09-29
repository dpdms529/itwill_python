#문제1) 임의의 정수가 짝수(2의 배수)인지 확인하시오
def isEven(num) :
    print('isEven(%d) : %s' % (num, num % 2 == 0))

isEven(2)   # True
isEven(1)   # False

#문제2) 임의의 정수가 3의 배수인지 확인하시오
def isMultipleOf3(num) :
    print('isMultipleOf3(%d) : %s' % (num, num % 3 == 0))

isMultipleOf3(6)    # True
isMultipleOf3(7)    # False

#문제3) 해당 년도가 윤년인지 확인하시오
def isLeapYear(year):
    print('isLeapYear(%d) : %s' % (year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0))

isLeapYear(2025)    # False
isLeapYear(2024)    # True

#문제4) 지폐의 갯수를 구하시오
"""
      만원 5장
      천원 4장
      백원 3장
      십원 2장 
"""

def countMoney(money):
    won_10000 = money // 10000
    print("만원 %d장" % won_10000)

    money %= 10000
    won_1000 = money // 1000
    print("천원 {}장".format(won_1000))

    money %= 1000
    won_100 = money // 100
    print("백원 {0}장".format(won_100))
    
    money %= 100
    won_10 = money // 10
    print("십원 {num}장".format(num=won_10))  

countMoney(54320)

#문제5) 임의의 정수가 2의 배수이면서 5의 배수인지 확인하시오
def isMultipleOf2And5(num) :
    print('isMultipleOf2And5(%d) : %s' % (num, num % 2 == 0 and num % 5 == 0))

isMultipleOf2And5(10)   # True
isMultipleOf2And5(6)    # False

#문제6) 임의의 정수가 1이거나 3인지 확인하시오.
def is1Or3(num) :
    print('is1Or3(%d) : %s' % (num, num == 1 or num == 3))

is1Or3(1)   # True
is1Or3(3)   # True
is1Or3(2)   # False

#문제7) 국어 점수가 80 ~ 89점 사이인지 확인하시오.
def isKorbetween80and89(kor) :
    print('isKorbetween80and89(%d) : %s' % (kor, 80 <= kor and kor <= 89))

isKorbetween80and89(85) # True
isKorbetween80and89(50) # False