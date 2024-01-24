print("python" + "Java")
print("python", "Java", sep=",")
print("python", "Java", sep=" vs ")

# end 로 적는거
print("python", "Java", sep=",", end="?")
print("무엇이 더  재밌을까요?")

# import sys 사용

import sys
print("python", "Java", file=sys.stdout) # 그냥 잘 나오는거
print("python", "Java", file=sys.stderr) # 표준 에러로 


# 출력포맷

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # subject, score 두개다 튜플로 할수있음
    # print(subject, score) # 보통 사용하는 방식
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기 순번표
# 001, 0002, 003, ...

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))


# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은" + answer + "입니다")
