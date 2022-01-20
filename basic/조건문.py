
'''
if 조건문 1: 
    조건문 1이 True일 때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당되지 않고, 조건문 2가 True일 때 실행되는 코드
else:
    위의 모든 조건문이 모두 True값이 아닐 때 실행되는 코드        
'''


# 성적 구간에 따른 학점 정보 출력

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
else:
    print("학점 : F")    

# 조건문에서 아무것도 처리하고 싶지 않을 때 pass를 이용할 수 있다

score = 85

if score >= 80:
    pass  # 나중에 작성할 코드
else:
    print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다")

# 한 줄에 적는 경우
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result)

# 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)


# 조건부 표현식을 사용하여 리스트의 값을 변경해서 또 다른 리스트를 만들 때
a = [1, 2, 3, 4, 5, 5, 6]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]

print(result)











