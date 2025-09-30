# 문제 1) 1부터 출력하다가 5가 되면 출력을 멈추시오
a = 1
while True:
    print(a)
    a = a + 1
    if a == 5:
        break

#문제2) 경로명, 파일명, 확장명을 각각 분리하여 변수에 저장하고 출력하시오
"""
    c:\myphoto
    helloworld
    jpg
"""
path = "c:\myphoto\helloworld.jpg"
idxSlash = path.rfind("\\")
dir = path[:idxSlash]
file, ext = path[idxSlash + 1:].split(".")

print(dir)
print(file)
print(ext)

#문제3) 다음식의 결과를 구하시오    
#->   1 - 2 + 3 - 4 + 5 ... + 100 = -50
flag = False
total = 0

for i in range(1, 101):
    if flag:
        flag = False
        total -= i
    else :
        flag = True
        total += i

print(total)

#문제4) x값이 10으로부터 x를 여러 번 뺀후
#      결과가 음수가 되면 x를 몇번 뺐는가를 구하시오
"""
    10 - 3 = 7
    7 - 3 = 4
    4 - 3 = 1
    1 - 3 = -2
"""
num = 10
x = 3
cnt = 0

while num > 0:
    num -= x
    cnt += 1

print(cnt)

#문제5) 3의 배수의 누적 합이 100이 넘어가려면
#      3부터 어디까지 더해야 하는지 구하시오
#      3 + 6 + 9 + 12 + 15 + 18 + 21 + 24
t = 3
sum = 0

while True:
    sum += t
    if sum <= 100:
        t += 3
    else:
        break

print(t)