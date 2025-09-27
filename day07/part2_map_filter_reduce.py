# part2_map_filter_reduce.py
# 고차함수란?
# 함수를 마치 인자, 인수, 값처럼 다루는 것을 가리키며
# 이 함수를 다른 함수에 전달하여 해당 함수 내에서 전달된 함수를
# 사용하는 것을 가리킨다.

# 람다함수, 익명함수를 마치 값처럼 함수의 인자로 전달하여
# 해당 외부 함수 내에서 동작을 수행시킬 수 있다.
# 이러한 것이 만들어진 함수의 종류가 map, filter, reduce인 것이다.

# 1. map
# 전달된 이터러블 객체의 각 요소에 적용시키고 싶은 동작을
# 함수로 작성하여 이터러블 객체와 함께 전달하면
# 해당 함수가 적용된 요소들로 이루어진 이터러블 객체를 반환한다.
# 이렇게 반환된 객체는 리스트나 튜플 등 다루기 편한 객체로 변환하여 주로 사용된다.
def part1_map():
    data = [1, 2, 3, 4, 5]
    # 전달된 값을 두 배로 늘려주는 함수
    doubled = lambda x: x * 2
    # 전달된 값을 두 배로 늘리는 함수를 전달하여
    # 각 요소를 모두 두 배가 된 요소들로 이루어진
    # 이터러블 객체를 만들어낸다.
    # 이때 전달하는 함수는 함수명만 혹은 람다식만 전달해야 한다.(사용x)
    doubled_data = map(doubled, data)
    # print(list(doubled_data))

    # 람다식을 직접 전달하는 방식
    doubled_data = map(lambda x: x**2, data)
    print(list(doubled_data))

# 2. filter
# 전달된 함수의 결과값에 따라서(T/F) True이면
# 해당 요소를 새로운 이터러블 객체에 포함시키고
# False이면 포함시키지 않는 동작을 수행한다.
def part2_filter():
    data = [1, 2, 3, 4, 5]
    # 조건식 활용한 람다식
    condition = lambda x: x % 2 == 0 # 짝수인지 여부
    # 짝수면 -> True, 홀수면 -> False
    filtered_data = filter(condition, data)
    # print(  list(filtered_data)  )

    # 람다식으로 직접 사용
    # 해당 조건식을 만족하는 요소만 복사하여
    # 새로운 데이터에 추가
    filtered_data = filter(  lambda x: x % 2 == 0  , data)
    print(  list(filtered_data)  )

def part3_sum():
    import math
    # 이미 만들어진 함수를 활용하여 map 사용
    # math.sqrt는 전달된 값 하나의 루트 값을 구하는 함수다.
    total = map(math.sqrt, list(range(1, 100)))
    # int()라는 함수는 정수형으로 형변환하는 함수다.
    # 함수명만 전달하는 것이므로, int라고만 작성해도 된다.
    total = map(int, total)
    print( list(total) )

def part4_reduce():
    # reduce 함수를 사용하려면 functools에서 가져와야 한다.
    from functools import reduce
    # reduce에 전달되는 함수는 두 개의 매개변수를 받아서
    # 그 결과를 첫번째 매개변수 대신에 사용하는 방식으로 동작한다.
    # 즉, 리스트를 전달할 경우, 0번째 요소는 x로 들어가고
    # 두번째 요소가 y로 들어간 뒤, 그 결과가 다음 요소를 사용할 때
    # 결과는 x 매개변수에, 다음 요소는 y에 들어가서 연산이 계속된다.
    # 최종적으로 결과값은 하나가 나오게 된다.
    add = lambda x, y: x+y
    # 1부터 10까지의 요소를 순차적으로 덧셈하여
    # 최종값 하나를 반환
    total = reduce(add, list(range(1,11)))
    # x=1, y=2 => 3
    # x=3, y=3 => 6
    # x=6, y=4 => 10
    # x=10, y=5 => 15
    # x=15, y=6 => 21
    # ...
    # reduce 함수의 특징은 결과값이 하나라는 사실이다.
    print(total) # 1부터 10까지의 합이 반환됨.

if __name__ == "__main__":
    # part1_map()
    # part2_filter()
    # part3_sum()
    part4_reduce()