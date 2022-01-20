a = [ 1, 4, 2, 3, 5, 3]
print("초기 값 : ", a)

# 리스트에 원소 삽입
a.append(6)
print("6 삽입 : ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 7)
print("인덱스 2에 7추가 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 수 세기 : ", a.count(3))

# 특정 값 데이터 1개 삭제
a.remove(3)
print("값이 3인 데이터 삭제 : ", a)  # 원소 1개만 사라진다

#  특정 값 데이터 1개 전체 삭제
a = [ 1, 2, 3, 3, 4, 5, 5, 5 ]
remove_set = [ 3, 5 ]

result = [i for i in a if i not in remove_set]
print(result)