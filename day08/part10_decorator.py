# part10_decorator.py
# 데코레이터
# 함수를 매개변수로 하여 전달하면 전달받은 함수 내에서
# 사용이 가능하다.
# 이를 이용해, 원본함수A의 바깥쪽에 다른 기능을 덧붙여서
# 꾸밈이 있는 함수를 실행하게 만드는 함수를
# 데코레이터라고 한다.
import time

# 데이레이터 함수
# 매개변수를 함수를 받을 변수 하나만 써야 한다.
def deco(func):
    def wrapper():
        # 추가로 실행하고 싶은 코드 작성
        before = time.time()
        func()
        time.sleep(2)
        after = time.time()
        print(f"걸린 시간: {after - before:.2f}s")
    return wrapper

# @와 함께 데코레이터 함수 이름을 작성하면
# 꾸밈 받는 함수가 데코레이터에 전달되어 꾸밈을 받고
# 재포장되어 반환된다.
@deco
def print_hello():
    print("hello")

if __name__ == "__main__":
    print_hello()