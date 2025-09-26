# 문제) 지폐의 갯수를 구하시오
money = 54320
"""
    만원 5 장
    천원 4 장
    백원 3 장
    십원 2 장
"""
won_10000 = money // 10000
print("만원 %d 장" % won_10000)
money %= 10000
won_1000 = money // 1000
print("천원 {} 장".format(won_1000))
money %= 1000
won_100 = money // 100
print("백원 {0} 장".format(won_100))
money %= 100
won_10 = money // 10
print("십원 {num} 장".format(num=won_10))                                                     