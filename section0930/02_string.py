# 문자열 관련 함수
str = "Life is too short. You need Python"
print(str)

# 글자 개수
print(len(str)) # 34

print(str.count('i'))       # 2
print(str.count('a'))       # 0
print(str.count('short'))   # 1
print(str.count('nice'))    # 0

print(str[3])   # e
print(str[0])   # L 문자열의 인덱스는 0부터 시작
print(str[-1])  # n -1은 마지막 글자
print(str[-3])  # h

# 특정 글자나 단어가 마지막으로 등장하는 위치 조회
print(str.rfind("i"))       # 5
print(str.rfind("a"))       # -1 찾고자 하는 문자열이 없을 때
print(str.rfind("short"))   # 12
print(str.rfind("nice"))    # -1

# 특정 글자나 단어가 처음 등장하는 위치 조회
print(str.index("short"))   # 12
# print(str.index("nice"))    # 에러 ValueError: substring not found

# 특정 단어나 글자로 시작하는지 여부 검사(True,False)
print(str.startswith("L"))      # True
print(str.startswith("l"))      # False
print(str.startswith("Life"))   # True
print(str.startswith("H"))      # False
print(str.startswith("Hello"))  # False

# 특정 단어나 글자로 끝나는지 여부(True,False)
print(str.endswith("N"))
print(str.endswith("n"))
print(str.endswith("Python"))
print(str.endswith("python"))

print(str.upper())      #전부 대문자로 변경       LIFE IS TOO SHORT. YOU NEED PYTHON
print(str.lower())      #전부 소문자로 변경       life is too short. you need python
print(str.swapcase())   #대소문자 서로 바꿔서     lIFE IS TOO SHORT. yOU NEED pYTHON
print(str.capitalize()) #문장의 첫글자만 대문자로  Life is too short. you need python
print(str.title())      #각 단어의 첫글자 대문자   Life Is Too Short. You Need Python

# 글자 치환 My height is too short. You need Python
print(str.replace("Life", "My height"))

# 공백제거
k = "    py th on  "
print("#" + k.lstrip() + "#")  #py th on  #
print("#" + k.rstrip() + "#")  #    py th on#
print("#" + k.strip() + "#")   #py th on#

# 문제) str변수의 문자열값에서 공백을 모두 제거하시오
print(str.strip().replace(' ', ''))

print(len(" ")) # 1
print(len(""))  # 0

# 문자열의 인덱싱 - 특정 위치의 글자를 추출
print(str[0])   #0번째문자 인덱스(순서)는 0부터 시작
print(str[3])   #3번째문자
print(str[-3])  #문자열 뒤에서 부터 시작
print(str[-1])  #문자열 맨 마지막 글자

# 문자열의 슬라이싱 - 특정 범위의 글자들을 추출
print("#" + str[0:3] + "#") #Lif#  0번째부터 (3-1)까지
print("#" + str[5:7] + "#") #is#
print("#" + str[19:] + "#") #You need Python#    19번째부터 마지막 까지
print("#" + str[:17] + "#") #Life is too short#  0번째부터 (17-1)까지

print("#" + str + "#")        #Life is too short. You need Python#
print("#" + str[:] + "#")     #Life is too short. You need Python#
print("#" + str[19:-7] + "#") #You need#

a = ","
print(a.join("PYTHON"))        #P,Y,T,H,O,N
#########################################################################

# 문제)주민번호에서 문자열 추출
#       출력결과
#       -> 출생년도 : 1989년
#       -> 출생월 : 12월
#       -> 출생일 : 03일
#       -> 성별코드 : 2
jumin = "8912032"
print(f"출생년도 : {('19' if int(jumin[6:]) < 3 else '20') + jumin[:2]}년")
print(f"출생월 : {jumin[2:4]}월")
print(f"출생일 : {jumin[4:6]}일")
print(f"성별코드 : {jumin[6:]}")

# 성별 코드에 따라 성별을 출력하시오
code = int(jumin[6:])
if code == 1 or code == 3:
    print("남자")
elif code == 2 or code == 4:
    print("여자")