# part6_class_coordinate.py
# 클래스 Coordinate를 이용하여 좌표 값의 덧셈과 뺄셈을 구현해보자.
# __add__, __sub__

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 좌항 coord의 x와 우항 coord의 x의 합
        result_x = self.x + other.x
        # 좌항 coord의 y와 우항 coord의 y의 합
        result_y = self.y + other.y
        # 각 좌표를 전달받아서 만들어지는 좌표 객체
        result = Coordinate(result_x, result_y)
        # 그 객체를 반환한다.
        return result
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    # 문자열 표현 바꾸기
    def __str__(self):
        return f"({self.x}, {self.y})" # (1, 3)

if __name__ == "__main__":
    a = Coordinate(1, 3)
    print(a)
    b = Coordinate(3, 5)
    print(b)
    print( a + b ) # (4, 6)
    print( a - b ) # (-2, -2)