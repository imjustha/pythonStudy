# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 적당한 제충

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#             *함수명 : std_weight
#             *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째짜리까지 표시

# (출력 에제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다

# (내 정답)

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21

height = int(input("키:"))
gender = input("성별;")
avg_weight = round(std_weight(height/100, gender),3)
print("키 {0}cm {1}의 표준체중은 {2}입니다".format(height, gender, avg_weight))
std_weight(input("성별:"), int(input("height:")))
input("")

# (정답)

# def std_weight(height, gender): # 키 m단위 (실수), 성별 "남자" / "여지"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 #cm 단위
# gender = "남자"
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))