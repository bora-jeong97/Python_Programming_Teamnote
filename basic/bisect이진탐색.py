# 정렬된 리스트에 새롭게 4를 삽입하려 할 때 해당 위치 값을 반환한다

from bisect import bisect_right, bisect_left

a = [1, 2, 4, 4, 8]
x = 4

print("bisect_left", bisect_left(a, x)) 
print("bisect_right", bisect_right(a , x)) 

'''
파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. 
bisect라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적이다.

- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 리스트 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드

- bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 리스트 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
'''

# left_value <= x <= right_value 인 원소의 개수를 O(logN)으로 계산

from bisect import bisect_right, bisect_left

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
