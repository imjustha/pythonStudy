gun = 10

def checkpoint(soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

# 위와 같이 하면 gun 이라는 함수가 할당이 안되었는데 쓸수없음 
# 함수안에서만 사용을 하려면 지역변수 밑에와 같이 쓰면 됨


gun = 10

def checkpoint(soldiers): #경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))



# 전역변수는 전체적으로 사용하게 함


gun = 10
def checkpoint(soldiers): #경계근무
    global gun # global을 쓰면 전역변수로 바뀜
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

# 하지만 전역변수는 많이 사용하지 않음 그래서  

gun = 10

def checkpoint(soldiers): #경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_rest(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_rest(gun, 2)
print("남은 총 : {0}".format(gun))