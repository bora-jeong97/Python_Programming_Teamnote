# 순열  : 순서가 있는 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열한 것
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))  # 모든 순열 구하기
print("3개 순열",result)

# 중복 순열
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print("중복 순열 ", result)

# 조합 : 순서 상관없이 서로 다른 n개에서 서로 다른 r개를 선택하는 것
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합
print("2개 조합",result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2)) # 중복 조합
print("중복 조합 ", result)