# 입력을 위한 전형적인 소스코드

# 데이터의 개수 입력 ex) 5
n = int(input())

# 각 데이터를 공백으로 구분하여 입력 ex) 1 7 3 5 2 입력
data = list(map(int, input().split()))

# 내림차순 정렬
data.sort(reverse=True)
print(data)


# 공백을 기준으로 적은 수의 데이터 입력받기 ex) 1 2 3
n, m, k = list(map(int, input().split()))

print(n, m, k)


# input()보다 더 빠른 readline()을 사용해 많은 양의 데이터를 빠르게 입력받기
# sys 라이브러리를 import해 사용하며 readline사용시 엔터가 줄바뀌기 때문에
# 공백 문자를 제거하려면 꼭 rstrip()함수를 써야한다

import sys

# 1 2 3 4 5 6 7 8 9 10 입력
data = sys.stdin.readline().rstrip()
print(data)


# 1) 정수형 변수를 문자열로 바꾸어 출력하는 소스코드 예시
answer = 7

print("정답은 " + str(answer) + "입니다.")

# 2) 각 변수를 콤마(,)로 구분하여 출력하는 예시
answer = 7

print("정답은", answer, "입니다.")

# 3) f-string 문법을 사용하는 예시
# Python 3.6 버전 이상부터 사용이 가능하다
print(f"정답은 {answer} 입니다.")