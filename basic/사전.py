# 사전자료형 선언 방법1
data = dict()

# 키와 값 입력
data['사전'] = 'Apple'
data['바나나'] = 'banana'
data['코코넛'] = 'Coconut'

print(data)


# 사전자료형 선언 방법2
data2 = {
    '빨강' : 'red',
    '주황' : 'orange',
    '파랑' : 'blue'
}

print(data2)

data3 = {
    1, 1, 2, 3, 4, 5
}


# 특정 원소 조회
if '빨강' in data2:
    print("'빨강'을 키로 가지는 데이터가 존재합니다")



data = {
    '빨강' : 'red',
    '주황' : 'orange',
    '파랑' : 'blue'
}

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키를 조회해서 값을 하나씩 출력
for key in key_list:
    print(data[key])

