# part3_list_comp.py
# 리스트 컴프리헨션(list comprehension)
# 직전에 배웠던 map과 filter를 리스트형태에 적합하게 만든
# 통합형 문법이다.
# [e for e in range(10)] -> list(range(10))
# 여기에 for 왼쪽의 표현식을 변경하면 map에서 함수를 전달한 것과 동일한
# 효과를 볼 수 있다.
# [e * 2 for e in range(10)] -> list(map(lambda x:x*2, range(10)))

# filter 효과를 넣으려면 이터 객체 우측에 if문을 작성하는 것으로
# 조건식의 결과에 따라 요소를 걸러낼 수 있다.
# [e * 2 for e in range(10) if e % 2 == 0]
# 2*2, 4*2, 6*2, 8*2
# [0, 4, 8, 12, 16]

def list_comp1():
    # 단순히 range를 이용하여 요소를 리스트로 만드는 동작
    # 리스트 컴프리헨션의 기본 형태
    # [e for e in range()]
    my_list = [e for e in range(10)] # [0-9]
    print(my_list)

def list_comp2():
    # map 기능을 리스트 컴프리헨션에서 사용해보자.

    # map 기능은 가장 왼쪽의 표현식 부분의 내용을 바꾸기만 하면 된다.
    my_list = [(e, 0) for e in range(10)]
    print(my_list)

# filter 기능을 if문을 활용하여 작성해보자.
# [e for e in range() if 조건식]
# if 뒤에 들어가는 조건식이 filter()에 전달되는 함수의 조건식과 같은 것이다.
# 이 조건식이 검사되는 타이밍은, 이터 객체에서 임시변수 e에 값이 전달된 뒤,
# if 조건식을 검사하여 그 결과가 참인 경우에만
# 가장 왼쪽의 표현식으로 전달되게 된다. 거짓인 경우에는 전달되지 않고
# 다음 요소로 넘어간다.
def list_comp3():
    # if문 사용
    # data = ["홍길동", 3, 3.14, True]
    my_list = [e*2 for e in range(10) if e % 2 != 0] # 홀수인 경우
    # isinstance(data[e], int)
    print(my_list)

if __name__ == "__main__":
    # list_comp1()
    # list_comp2()
    list_comp3()