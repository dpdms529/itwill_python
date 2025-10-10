# 파일 입출력
# -> r : 읽기모드
# -> w : 쓰기 모드(overwrite 덮어쓰기)
# -> a : 추가 모드(append 추가)

# 1) 파일 쓰기
# -> 대상 파일이 없으면 생성(create)
f = open("./section1010/helloworld.txt", "w", encoding="utf-8")
f.write("Hello Python!!\n\n")
f.write("안녕하세요~~ 파이썬!!\n")
f.close()

print("helloworld.txt 완성!!!")
########################################################################

# 2) 파일 읽기
# -> 대상 파일이 존재하지 않으면 에러 발생
# f = open("./section1010/hello.txt", "r", encoding="utf-8") # FileNotFoundError: [Errno 2] No such file or directory: './section1010/hello.txt'
f = open("./section1010/helloworld.txt", "r", encoding="utf-8")
print(f.read())
# End Of File(EOF) : 파일의 끝
f.close()
########################################################################

# 3) 추가 모드로 파일 객체 생성
with open("./section1010/helloworld.txt", "a", encoding="utf-8") as f:
    for i in range(1, 10):
        f.write("%d >> " % i)
        f.write("Life is too short,")
        f.write("you need Python\n")
print("helloworld.txt 완성!!!")
########################################################################

# 4) 읽기 모드로 파일 객체 생성하기
with open("./section1010/helloworld.txt", "r", encoding="utf-8") as f:
    # data = f.read()  # 파일의 끝(EOF)을 만날 때까지 한 글자씩 가져오기
    # print(data)
    while True:
        line = f.readline()  # 엔터를 기준으로 가져오기
        if not line:
            break
        print(line.strip())
