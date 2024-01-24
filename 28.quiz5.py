# Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사이다
# 50명의 승객과 매칭기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1: 승격별 운행 소요시간은 5분~50분 사이의 난수로 정해집니다
# 조건2: 당신은 소요시간 5분~15분 사이의 승객만 매칭해야 합니다

# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객: 2분

# 내 정답
from random import *
customer = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        customer += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(customer))

# 정답
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~50 이라는 수 (승객)
    time = randrange(5, 51) # 5분~ 50분 소요시간
    if 5 <= time <= 15: #5분 ~ 15분 이내의 손님, 탑승 승객수 증가처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))