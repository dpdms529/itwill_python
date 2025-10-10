"""
- 프로그램이 실행 중 오류가 발생했을때 -> 예외상황
- 예외상황이 발생하면 코드 진행이 중단되므로 계속 진행할 수 있도록 선언
- Exception이 발생하더라도 정상적으로 프로그램은 종료시킬 수 있다
- 형식) try:
             문제가 없을 시 실행할 코드
        except:
             문제 발생(예외상황)시 실행할 코드
"""

# 1. 예외처리 하지 않은 경우
"""
print("START")
print(1)
print(3 / 0)  # ZeroDivisionError: division by zero
print(5)
print("END")
"""

# 2. 예외처리를 한 경우
print("START")
try:
    print(1)
    print(3 / 0)  # ZeroDivisionError: division by zero
    print(5)
except Exception as e:
    print(f"예외발생: {e}")
print("END")

# 3. try except else
# -> except가 발생하지 않으면 else 실행
print("START")
try:
    print(1)
    result = 3
    print(5)
except Exception as e:
    print(f"예외발생: {e}")
else:
    print(f"result: {result}")
print("END")

# 4. try except finally
# -> except 발생 유무와 상관없이 finally 구문 실행
print("START")
try:
    print(1)
    result = 3 / 0
    print(5)
except Exception as e:
    print(f"예외발생: {e}")
else:
    print(f"result: {result}")
finally:
    print("연산종료")
print("END")
