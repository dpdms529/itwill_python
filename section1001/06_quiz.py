# 문제) string타입 데이터를 입력 받았을 때 문자열 가운데를 출력하시오

text = input("Type text : ")
print(text)
print(type(text))

# 예) korea -> r
# 예) itwill => wi


def getMid():
    n = len(text) // 2

    if n % 2 == 0:
        return text[n : n + 1]
    else:
        return text[n - 1 : n + 1]


print(getMid())


# 투포인터
def getMidTwoPointer():
    start, end = 0, len(text) - 1

    while start < end:
        start += 1
        end -= 1

    return text[end : start + 1]


print(getMidTwoPointer())


# 재귀
def getMidRecursion(text, start, end):
    if start >= end:
        return text[end : start + 1]
    else:
        return getMidRecursion(text, start + 1, end - 1)


print(getMidRecursion(text, 0, len(text) - 1))
