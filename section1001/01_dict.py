# 연속형 자료형
# Dictionary 딕셔너리
# -> 이름(key, name)과 값(value)의 쌍으로 데이터를 정의하는 구조
# -> 순서가 없다
# -> {key:value, key:value, ...}

dic = {"name": "무궁화", "phone": "123-4567", "birth": "202510101"}
print(dic)  # {'name': '무궁화', 'phone': '123-4567', 'birth': '202510101'}
print(type(dic))  # <class 'dict'>
print(dic["name"])  # 무궁화
print(dic["phone"])  # 123-4567

dic["name"] = "라일락"
print(dic["name"])  # 라일락

# 삭제
del dic["birth"]
print(dic)  # {'name': '라일락', 'phone': '123-4567'}

data = {"msg": "Hello", "msg": "World", "msg": "Python"}
print(data)  # {'msg': 'Python'}

# 딕셔너리는 리스트와 다르게 자료의 순서가 중요하지 않다
# key는 정수형으로도 지정 가능(리스트와 혼동될 수 있으므로 권장하지 않음)
rank = {0: "Python", 30: "Java", 10: "Oracle"}
print(rank[0])  # Python
print(rank[30])  # Java
print(rank[10])  # Oracle
######################################################################

# 1) 딕셔너리의 계층 구조
# -> 딕셔너리는 리스트나 다른 딕셔너리를 포함할 수 있다.
# -> 정보를 계층화해서 표현 가능하다

addr = ["서울", "서초구", "강남대로"]
grade = {"korean": 10, "math": 20, "english": 30}
member = {"userid": "Python", "age": 2, "addr": addr, "grade": grade}
print(member)

# 계층화된 값에 접근하기
print(member["addr"][0])  # 서울
print(member["grade"]["korean"])  # 10

# 2) 딕셔너리의 계층화 직접 표현
mydic = {
    "total": 2025,
    "city": ["서울", "제주", "부산"],
    "population": [100, 200, 300],
    "date": {"yy": 2025, "mm": 8, "dd": 25},
}

print(mydic)
print(mydic["city"][0])  # 서울
print(mydic["population"][0])  # 100
print(mydic["date"]["yy"])  # 2025

# 3) 리스트의 요소가 딕셔너리가 되는 경우 -> 표 자료형
grade = [
    {"name": "홍길동", "kor": 10, "eng": 40},
    {"name": "무궁화", "kor": 20, "eng": 60},
    {"name": "라일락", "kor": 30, "eng": 90},
]

style = "{}의 국어점수:{}, 영어점수:{}"
print(style.format(grade[0]["name"], grade[0]["kor"], grade[0]["eng"]))
# 홍길동의 국어점수:10, 영어점수:40

print(style.format(grade[1]["name"], grade[1]["kor"], grade[1]["eng"]))
# 무궁화의 국어점수:20, 영어점수:60

print(style.format(grade[2]["name"], grade[2]["kor"], grade[2]["eng"]))
# 라일락의 국어점수:30, 영어점수:90
######################################################################

# 딕셔너리 관련 함수
dic = {"name": "무궁화", "phone": "123-4567", "birth": "202510101"}
print(dic)

# 특정 key에 대응하는 값 얻기
# -> dic["name"] 과 동일
print(dic["name"])
print(dic.get("name"))

# 존재하지 않는 key 에 접근하는 경우
# print(dic["age"])  # KeyError: 'age'
print(dic.get("age"))  # None

dic["addr"] = "Seoul"
print(dic["addr"])
print(dic)

# get함수는 전달하는 key가 존재하지 않을 경우
# 대신 반환될 값을 함께 설정할 수 있다
print(dic.get("age", 25))  # 25

keys = dic.keys()
print(keys)  # dict_keys(['name', 'phone', 'birth', 'addr'])

key_list = list(keys)
print(key_list)  # ['name', 'phone', 'birth', 'addr']
print(key_list[1])  # phone

values = dic.values()
print(values)  # dict_values(['무궁화', '123-4567', '202510101', 'Seoul'])

value_list = list(values)
print(value_list)  # ['무궁화', '123-4567', '202510101', 'Seoul']
print(value_list[1])  # 123-4567

# key-value를 쌍으로 묶은 튜플들의 모음인 items 객체 얻기
items = dic.items()
print(items)
# dict_items([('name', '무궁화'), ('phone', '123-4567'), ('birth', '202510101'), ('addr', 'Seoul')])

items_list = list(items)
print(items_list)
# [('name', '무궁화'), ('phone', '123-4567'), ('birth', '202510101'), ('addr', 'Seoul')]
print(items_list[1])  # ('phone', '123-4567')
