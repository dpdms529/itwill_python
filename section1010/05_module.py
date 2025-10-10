# 클래스가 정의된 모듈 참조하기
# 모듈 파일 my_module.py 작성

## 1)
import my_module

mem = my_module.Member("kim", "kim@itwill.com")  # Member 클래스 생성자 호출됨...
mem.disp()  # 이름 : kim / 이메일 : kim@itwill.com

## 2) 별칭 적용
import my_module as mm

mem = mm.Member("lee", "lee@itwill.com")  # Member 클래스 생성자 호출됨...
mem.disp()  # 이름 : lee / 이메일 : lee@itwill.com

## 3) 특정 클래스만 가져오기
from my_module import Member

mem = Member("park", "park@itwill.com")  # Member 클래스 생성자 호출됨...
mem.disp()  # 이름 : park / 이메일 : park@itwill.com
