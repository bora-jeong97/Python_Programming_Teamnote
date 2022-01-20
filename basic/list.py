# 리스트 선언
a = [1, 2, 3, 4, 5, 6, 7]
print(a)

# 인덱스 3 접근 == 4번째 원소 접근
print("인덱스 3 : ", a[3])

# 빈 리스크 선언법1.
a = list()
print("빈 리스크 : ", a)

# 빈 리스크 선언법2.
b = []
print("빈 리스크2 : ", a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * 10
print("초기화 : ", a)

# 인덱싱 : 특정 원소에 접근, -1은 그 마지막 원소가 출력된다
a = [ 1, 2, 3, 4, 5]
print("a[-1] : ", a[-1])

# 인덱싱 값 변경
a[-1] = 7
print("변경된 a[-1]의 list값 : ", a)


# 슬라이싱 : 연속된 위치를 갖는 원소를 가져올 때 사용한다
# 대괄호 안에 콜론(:)을 넣어 시작 인덱스와 끝 인덱스-1을 설정한다
a = [ 1, 2, 3, 4, 5, 6, 7 ]
print(a[ 0 : 3 ])  # 첫번째 원소부터 3번째 원소까지 출력

# 리스트 컴프리헨션 :  리스트를 초기화하는 방법 중 하나로 대괄호([ ]) 안에 조건문과 반복문을 넣는 방식이다.
# 0부터 19까지의 수 중에서 짝수만 포함하는 리스트
# Ex1. 여기서 range의 start는 1부터 시작하며 end는 n-1이다
array = [ i for i in range(20) if i % 2 == 0 ]
print(array)

# 위 소스코드를 일반적인 소스코드로 작성시 다음과 같다
array = []
for i in range(20):
    if i % 2 == 0:
        array.append(i)

print(array)        


# Ex2. 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [ i * i for i in range(1, 10)]
print(array)

# Ex3. N * M 크기의 2차원 리스트 초기화
# 언더바(_)는 반복을 위한 변수를 무시하기 위해 사용된다
n = 3
m = 4
array = [ [0] * m for _ in range(n)]
print(array)





