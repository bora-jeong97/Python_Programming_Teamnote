
# sum : iterable 객체가 입력으로 주어질 때모든 원소의 합을 반환
# * iterable : 반복 가능한 객체. ex) 리스트, 튜플, 사전자료형 등

result = sum([1, 2, 3, 4, 5])
print("sum : ", result)


# min : 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환

result = min(7, 3, 2, 1)
print("min : ", result)


# min : 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환

result = max(7, 3, 2, 1)
print("max : ", result)


# eval : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다

result = eval("(3 + 5) * 7")
print("eval : ", result)


# sorted : iterable 객체가 입력으로 주어질 때모든 원소의 합을 반환
#          기본은 오름차순, reverse = True : 내림차순 

result = sorted([9, 1, 2, 5, 3])
print("오름차순 정렬 : ", result)
result = sorted([9, 1, 2, 5, 3], reverse=True)
print("내림차순 정렬 : ", result)


# 리스트의 원소로 리스트나 튜플이 존재할 때 key속성을 정렬기준으로 명시할 수 있다

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x : x[1], reverse=True)
print(result)


# iterable 객체는 기본으로 sort()를 내장하고 있어 굳이 sorted()함수를 사용하지 않고도 정렬할 수 있다

data = [9, 1, 3, 5, 4]
data.sort()
print(data)