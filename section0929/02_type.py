# Data Type(자료형) 조회
print(type(123))        # <class 'int'> 정수형
print(type(4.5))        # <class 'float'> 실수형
print(type('Hello'))    # <class 'str'> 문자형
print(type(True))       # <class 'bool'> 논리형

print(type([1, 3, 5]))         # <class 'list'> 리스트
print(type((2, 4, 6)))         # <class 'tuple'> 튜플
print(type({"name":"ITWILL"})) # <class 'dict'> 딕셔너리
############################################################

# Datatype Conversion 형 변환
# -> 형식: 자료형(값)
x = 3
y = 4.5
z = float(x)
w = int(y)

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(w, type(w))
############################################################

# == 과 is 연산의 차이
i = 100    # 정수형
j = 100.0  # 실수형

# 단순히 값만 비교하므로 두 값이 같다고 판단
print(i == j)   # True

# 값의 종류(데이터타입)까지 비교하므로
# -> 정수와 실수는 다르다고 판단
print(i is j)   # False