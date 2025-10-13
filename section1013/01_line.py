# 선그래프
# -> 한가지 지표에 대한 특정 기준
# -> (주로 시간)에 따른 변화

# matplotlib 패키지
# ->데이터를 차트나 플롯(Plot)으로 그려주는 패키지

# matplotlib 패키지 설치
# >pip install matplotlib

import numpy as np
from matplotlib import pyplot as plt

# 1)
data = [10, 11, 12, 13, 14]

# 그래스 설정 시작
# -> 모든 그래프 작업 시작시 호출
plt.figure()

# 데이터를 선그래프로 표현
# ->리스트의 각 값은 y축이 되고,
# ->리스트 값의 인덱스는 x축이 된다.
plt.plot(data)
# 그래프 표시하기
plt.show()
# 그래프 관련 설정 해제
plt.close()
