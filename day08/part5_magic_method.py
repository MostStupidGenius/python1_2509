# part5_magic_method.py
# 매직 메서드
# 파이썬에서 미리 만들어놓은 메서드들로, 특정한 동작이나 연산을 수행하기 위한
# 특별한 메서드들이다.

# 객체생성
# __init__
# __new__

# 객체 해제(삭제)
# __del__
class Person():
    def __init__(self):
        print("init")
        self.age = 30
    
    # new 매직 메서드는 init 매직 메서드 대신에 동작하기 때문에
    # init이랑 같이 있다면 init은 동작하지 않는다.
    # def __new__(cls):
    #     print("new")
    #     print(cls)
    #     print("=" * 20)

    # 객체를 삭제할 때 호출되는 메서드
    def __del__(self):
        print("del")

    # 특정 속성(attribute)을 제거할 때
    # 해당 변수명을 name 매개변수로 전달하여 실행되는 메서드다.
    def __delattr__(self, name):
        print(f"del {name}")

    # 객체의 문자열 표현
    def __str__(self)->str:
        result = super().__str__()
        # 재정의(오버라이드)
        result = f"{self.age}살 객체"
        # print(result)
        return result

    # 공식적인 문자열 표현
    # representation(대표)
    def __repr__(self) -> str:
        return "대표"

if __name__ == "__main__":
    p = Person()
    # p 객체 삭제
    print(p.age)
    
    # 지우기 전에 문자열 출력
    # print(p)
    print(str(p))
    print(repr(p))
    print(p)

    del p.age
    del p
    pass