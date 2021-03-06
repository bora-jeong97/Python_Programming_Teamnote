# 그리디 알고리즘(탐욕법) 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 1. 거스름돈 500 100 50 10 거술러 줄 돈 N
# 가장 큰 화폐 단위부터 돈을 거슬러 준다.
# 가장 큰 단위가 작은 단위의 배수이면 가능하다. ex) 500 400 100은 안된다.
# 거스름 돈 : 시간 복잡도 O(k)

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 몫, 거슬러 줄 수 있는 동전의 개수 ex)count = 2
    n %= coin  # 1260 / 500 나눈 나머지 n = 260

print(count)   # 총 거슬러줄 동전 수 500 * 2 100 * 2 50 *1 10 *1  



# 2. n이 1이 될 때까지
# n과 k를 공백 기준으로 입력받기
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # k로 나눠떨어지는 수 10 // 3 * 3 = 9
    result += (n - target) # -1을 몇번 해야하는 지 횟수 추가 10 - 9 = 1 
    n = target # n = 9

    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    # k로 나누기
    n //= k  # n = 3
    result += 1  # 바로 위 k로 나눈 연산 1번을 카운트 해준다

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)  # 총 계산한 횟수를 결과값으로 반환
























