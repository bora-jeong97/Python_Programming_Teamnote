
# while
# 조건문이 참일 때에 한해서 반복적으로 코드가 수행된다

i = 1
result = 0

# i가 9보다 작거나 같을 때 홀수 값을 반복해서 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)        


# for
# in 뒤에 오는 모든 원소를 첫번째 인덱스부터 하나씩 방문한다
# in 뒤에는 리스트, 튜플, 문자열 등이 올 수 있다.

result = 0

# i는 1부터 9까지 모든 값을 순회
for i in range(1, 10):
    result += i

print(result)    

# continue : continue를 만나면 반복문의 처음 시작으로 돌아간다

scores = [90, 85, 77, 65, 92]
cheating_list = [2, 4]

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다")

