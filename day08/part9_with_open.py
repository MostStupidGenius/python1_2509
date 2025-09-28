# part9_with_open.py
# with open(): 코드블록을 이용하는 방법
# open을 하면 close를 꼭 해줘야 했는데,
# 이를 자동으로 열고 닫아주는 코드블록 문법이 있다.
# with open() as f: 코드 블록이다.

def read_with(file_name="test2.txt"):
    # with문을 사용하면 file 객체를 자동으로 열고 닫을 수 있다.
    content = None
    with open(file_name, 'r', encoding='utf-8') as f:
        # as f의 f가 이전의 file 객체로 취급된다.
        # with: 코드블록이 끝나면 자동으로 객체를 해제된다.
        content = f.read()
        print(content)
    return content

if __name__ == "__main__":
    content = read_with()
    print("읽어온 내용\n", content)