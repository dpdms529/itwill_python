# numpy 모듈
# -> 리스트의 기능 강화판. 과학 계산을 위한 라이브러리.
# -> 다차원 배열을 처리하는데 필요한 여러 기능을 제공하고 있다.
# 배열 Array : 데이터를 모아놓은 자료구조
# -> 리스트, 튜플, 딕셔너리 등

"""
설치 모듈 확인
>pip list

numpy 모듈 설치
>pip install numpy

numpy 모듈 삭제
>pip uninstall -y numpy
"""

import numpy as np

arr = [1, 2, 3]
print(arr)  # [1, 2, 3]
print(len(arr))  # 3

# 리스트 값을 1차원 배열 만들기
a = np.array(arr)
print(a)  # [1 2 3]
print(len(a))  # 3
print(type(a))  # <class 'numpy.ndarray'>

# 실수가 범위가 더 크므로 모든 요소가 실수형으로 변환
b = np.array([1, 2.3, 4, 5.6])
print(b)  # [1.  2.3 4.  5.6]

# 모든 타입이 문자열로 변환
c = np.array([1.2, 3, "4"])
print(c)  # ['1.2' '3' '4']

d = np.array([1, 2.3, 4, 5.6], dtype="int")
print(d)  # [1 2 4 5]

e = np.array([1, 2.3, 4, 5.6], dtype="float")
print(e)  # [1.  2.3 4.  5.6]

# enumerate() : 반복문에서 인덱스(index)와 값(value)을 동시에 가져올 때
for idx, v in enumerate(e):
    print(f"{idx}번째 요소 : {v}")
"""
0번째 요소 :  1.0
1번째 요소 :  2.3
2번째 요소 :  4.0
3번째 요소 :  5.6
"""
