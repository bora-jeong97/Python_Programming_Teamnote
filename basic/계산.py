# sum()
result = sum([1, 2, 3, 4, 5])
print("1부터 5까지의 합: ",result)

# min() max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print("작은 수 , 큰수 : ",min_result, max_result)

# eval() : 식을 수로 변환해서 결과값을 보여준다
result = eval("(3+5)*7")
print(result)

# sorted() : 정렬
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)  # 오름차순
print(reverse_result)  # 내림차순

# sorted() withe key 튜플 형태에 있을 때 2번째로 정렬한다면
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)  # 1로 넣어서 숫자 오름차순 정렬


#Counter : 등장 횟수 세기
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green']) 
print(dict(counter)) # 사전 자료형으로 변환

# 최대 공약수 math라이브러리의 gcd()함수 이용
import math

a = 21
b = 14

print(math.gcd(a, b)) # 최대 공약수 계산

#최대 공배수(LCM) 계산
def lcm(a, b):
    return a * b // math.gcd(a, b)  # 두 수의 곱을 최대 공약수로 나눈 것

print(lcm(a, b))













