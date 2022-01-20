# Ex2. x만큼 간격이 있는 n개의 숫자
# 입력
x, n = map(int, input().strip().split(' '))

def solution(x, n):
    answer = []
    # 반복문
    for i in range(n):
        answer.append(x+x*i)
    return answer

#def solution(x, n):
#   return [i * x + x for i in range(n)]


# 출력
print(solution(x, n))