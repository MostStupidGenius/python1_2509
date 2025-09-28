# part7_file_handling.py
# 파일 입출력
# 텍스트 파일을 파이썬 코드를 이용하여 작성하고 읽어올 수 있다.
# 이를 통해 콘솔에서만 존재하던 정보를 반영구적으로 저장하고
# 읽어오는 동작이 가능해진다.

# 기본적으로 파일에 접근하려면 'open()'를 사용해야 한다.
# 이를 이용해 파일 객체를 불러오고 파이썬 코드와 파일 시스템이
# 연결되어 읽기/쓰기 작업이 가능해진다.

def read_file(file_name:str="test.txt"):
    # 파일 객체 생성
    # open(파일경로문자열, 모드)
    # 파일에 접근할 때에는 읽기를 할지, 쓰기를 할지,
    # 이어쓰기를 할지 등을 정해주어야 한다.
    # 'r': 읽기 전용
    # 'w': 덮어쓰기, 파일이 없으면 생성하고 처음부터 쓴다.
    # 파일이 있으면 모든 내용을 삭제하고 처음부터 쓴다.
    # 'a': 이어쓰기, 파일이 없으면 생성
    # 있으면 이어서 쓴다.
    file = open(file_name, 'r', encoding="utf-8") # 읽기 모드로 연다
    # 읽기 작업
    # .read()를 쓰면 모든 내용을 한번에 읽어온다.
    content = file.read()
    file.close() # 다음 동작을 위해서 파일을 미리 닫는다. 
    print(content)
    # file.read나 .readline 등의 동작을 하면
    # 데이터를 한번 읽어왔기 때문에
    # 같은 내용을 같은 파일 객체에서 반복적으로 읽어올 수는 없다.

    file = open(file_name, 'r', encoding='utf-8')
    # .readline()을 쓰면 모든 내용을 행 단위로 나눠서
    # 문자열 리스트로 반환한다.
    lines = file.readlines()
    # 모든 라인 출력
    for e in lines:
        print(e, end="") # 줄바꿈 제거
        # 기본 line마다 줄바꿈이 맨 마지막에 들어가 있기 때문이다.
    file.close()

# 파일 쓰기
# 파일은 쓰기 모드가 두 가지 있는데,
# 공통적으로 파일이 없으면 새로 생성한 뒤 작성된다.
# w 모드는 기존 내용이 있으면 비운 뒤(truncate)
# 내용을 작성한다.
# a 모드는 append 모드이기 때문에
# 기존 내용에 이어서 작성된다.
def write_file(file_name="test2.txt", mode="w"):
    # file 객체 만들기
    file = open(file_name, mode, encoding='utf-8')
    # 파일에 쓰기 작업
    length = file.write("새로운 내용1\n새로운내용 두번째줄\n")
    print(f"length: {length}")
    file.close()
    pass


if __name__ == "__main__":
    # read_file()
    # write_file(mode="a") # 추가 모드로 작성
    # 없는 파일을 읽으려고 할 때 문제가 발생한다.
    read_file("없는파일.txt")