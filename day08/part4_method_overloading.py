# part4_method_overloading.py
# 오버로딩(overloading)
# 메서드를 정의할 때 매개변수에 기본값을 설정하면
# 전달하는 인자, 인수(값)의 개수를 조정할 수 있다.
# 이를 통해서 하나의 메서드에 대해서 서로 다른 동작을 하게 만들 수 있다.

# 생성자 오버로딩
class Person():
    # 기본 생성자
    def __init__(self, age, name=None, *args, **my_dict): # 매개변수명만 작성하면
        # 반드시 그 값을 전달받아야 한다.
        # 매개변수명 뒤에 할당연산자를 사용하여 기본값을 세팅하면
        # 입력을 받지 않더라도 기본값이 대신 세팅된다.
        # 기본값을 세팅하지 않은 매개변수를 먼저 작성하고,
        # 그 다음에 기본값을 세팅한 매개변수를 작성해야 한다.(순서 중요)
        self.age = age
        self.name = name or "이름없음"
        # print(type(args))
        # print(args)
        # print(type(my_dict))
        print(  my_dict  )
        pass
    pass

if __name__ == "__main__":
    p = Person(30, "홍길동", "서울시", b="기타", a="책읽기")
