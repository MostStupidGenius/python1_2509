# part11_iterator.py
# 이터레이터
# 이터러블 객체를 일회성 이터레이터로 만들어서 
# 그 요소를 순차적으로 하나씩 가져오기 위해 만드는 객체다.

if __name__ == "__main__":
    my_list = [e for e in range(100) if e % 3 == 0]
    iter_list = iter(my_list) # 이터러블로 만들기
    e = next(iter_list)
    print(e)
    while e:=next(iter_list, None):
        print(e)