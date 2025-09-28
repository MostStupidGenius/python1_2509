# part2_class_using.py
# 클래스 사용해보기

# 클래스 이름 뒤의 소괄호는 상속받고자 하는 부모 클래스 이름이 들어갈 공간인데
# 상속이 필요없다면 소괄호를 생략할 수 있다.
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    # self.변수명으로 설정한 속성들은 메서드에서 self를 매개변수로 받을 때
    # self를 통해서 접근할 수 있다.
    def access_self(self):
        print(f"제 이름은 {self.name}이구요, 나이는 {self.age}살입니다.")


if __name__ == "__main__":
    hong = Person("홍길동", 30)
    lee = Person("이순신", 50)
    hong.access_self() # 제 이름은 홍길동이구요...
    lee.access_self() # 제 이름은 이순신이구요...