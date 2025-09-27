# part3_function2.py
# 함수는 매개변수가 있을 수도, 없을 수도 있으며
# 반환값(return)이 있을 수도 없을 수도 있다.

# 모든 경우의 함수를 만들어보며 익혀보자.

# 1. 매개변수x, 반환값x
# 정해진 문장을 출력하는 함수
def no_param_no_return() -> None:
    print("전달받은 값이 없는 함수")

# 2. 매개변수o, 반환값x
# 성과 이름을 전달받아서 병합한 이름을 출력하는 함수
def print_full_name(fname, lname) -> None:
    print(f"{fname}{lname}")
    return # 값 없이 return을 사용하면 함수가 조기종료된다.

# 3. 매개변수x, 반환값o
# 이름을 반환하는 함수
def get_name() -> str:
    return "이준상"

# 4. 매개변수o, 반환값o
# 숫자 두 개를 전달받아서 그 합을 반환하는 함수
def add(num1:float|int, num2:float|int) -> float:
    result = num1 + num2
    return result
# 숙제
# 두 개의 숫자를 전달받아서 그 차, 곱, 나눗셈을 수행한 결과를 반환하는 함수

# sub()
def sub(num1:float, num2:float) -> float:
    result = num1 - num2
    return result
# multi()
def multi(num1:float, num2:float) -> float:
    result = num1 * num2
    return result

# div()
def div(num1:float, num2:float) -> float:
    # 0으로 나눴을 때 오류가 발생할 수 있으므로
    # num2의 값이 0일 때 0을 반환하도록 처리한다.
    if num2 == 0: return 0
    # num2의 값이 0일 경우, return 0을 수행하므로
    # 함수가 종료되어 아래의 코드가 실행되지 않는다.
    # num2의 값이 0이 아니라면 위의 if문을 건너뛰고
    # 아래의 코드가 실행될 것이다.
    result = num1 / num2
    return result

if __name__ == "__main__":
    # 1. 매개x 반환x
    no_param_no_return()
    # 2. 매개o, 반환x
    print_full_name("홍", "길동")
    print_full_name("제갈", "공명")
    # 3. 매개x, 반환o
    name = get_name() # "이준상"
    # print(name)
    
    # 4. 매개o, 반환o
    result = add(33, 77)
    print(result) # True
