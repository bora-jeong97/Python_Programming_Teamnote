'''
        def 함수명(매개변수):
            실행할 소스코드
            return 반환 값
'''
# return 값 사용
def add(a, b):
    return a + b

print("함수의 결과 : ", add(1, 2))    


# return 값 미사용
def add(a, b):
    print("함수의 결과 : ", a + b)

add(1, 2) 

# 매개변수의 순서를 다르게 사용 할 수 있다

def add(a, b):
    print("함수의 결과 : a 는 {} b 는 {}".format(a, b))

add(b=3, a=2)    

# 함수 안에서 함수 밖의 변수를 쓸 수 있다

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)    

# 파이썬에는 람다식 표현으로 add()메서드를 구현할 수 있다
print((lambda a, b: a + b)(3, 7))