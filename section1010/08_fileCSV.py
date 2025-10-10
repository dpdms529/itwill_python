# .csv: 데이터가 , 기호를 기준으로 구성된 파일

grade = [
    {"name": "홍길동", "kor": 90, "eng": 85, "mat": 100},
    {"name": "무궁화", "kor": 30, "eng": 80, "mat": 90},
    {"name": "라일락", "kor": 60, "eng": 55, "mat": 70},
]

style = "{0}, {1}, {2}, {3}\n"

# 1) CSV 파일 쓰기
with open("./section1010/grade.csv", "w", encoding="utf-8") as f:
    for g in grade:
        f.write(style.format(g["name"], g["kor"], g["eng"], g["mat"]))

print("grade.csv 파일 완성!!")

# 2) CSV 파일 읽기
with open("./section1010/grade.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        std = i.strip().split(",")
        name = std[0]
        kor = int(std[1])
        eng = int(std[2])
        mat = int(std[3])
        total = kor + eng + mat
        avg = total / 3
        print(f"{name} {kor} {eng} {mat} {total} {avg:.2f}")
