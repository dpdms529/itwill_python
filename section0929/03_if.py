# 제어문 : 프로그램의 흐름을 제어
# -> 조건문과 반복문
"""
    - 파이썬의 코딩블럭
      코딩블럭을 표시하기 위해 들여쓰기(Identation)을 사용
      일반적으로 들여쓰기에는 4개의 공백을 사용할 것을 권장
      동일한 블럭의 들여쓰기는 모두 동일한 수의 공백을 사용해야 함
      주의할 점은 공백과 탭을 혼용해서 사용하지 말아야 함
"""
"""
    - if 조건문의 형식

      if 조건: 조건이 True일때 처리명령어


      if 조건:
                조건이 True일때 처리명령어
      else:
                조건이 False일때 처리명령어


      if 조건1:
                     조건1이 True일때 처리명령어
      elif 조건2:
                     조건2가 True일때 처리명령어
      elif 조건3:
                     조건3이 True일때 처리명령어
      else:
                     조건이 False일때 처리명령어
"""

#문제1) 절대값을 구하시오 (무조건 양수)
abs = -3

if abs > 0:
    print(f"{abs} -> {abs}")
else :
    print(f"{abs} -> {-abs}")

#문제2) 임의의 값이 양수, 음수, 제로를 출력하시오
num = 0

if num > 0:
    print(f"{num} : 양수")
elif num == 0:
    print(f"{num} : 제로")
elif num < 0:
    print(f"{num} : 음수")

#문제3) 세개의 수중에서 최대값을 출력하시오
a = -2
b = -8
c = -9

max = 0

if a > b:
    max = a
    if max < c:
        max = c
else:
    max = b
    if max < c:
        max = c
print(f"max : {max}")

#문제4) 성별코드에 따라 나이와 성별을 출력하시오
myYear = 10
myCode = 4

if myCode < 3:
    age = 2025 - (1900 + myYear)
    if myCode % 2 == 0:
        print(f"age : {age}, gender : female")
    else:
        print(f"age : {age}, gender : male")
else:
    age = 2025 - (2000 + myYear)
    if myCode % 2 == 0:
        print(f"age : {age}, gender : female")
    else:
        print(f"age : {age}, gender : male")