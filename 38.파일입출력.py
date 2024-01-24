score_file = open("score.txt", "w" , encoding="utf8") # w = write 목적 덮어쓰기가 됨
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일을 열면 항상 닫아야함

score_file = open("score.txt", "a" , encoding="utf8") # a= append 뒤에다가 바로 이어서 쓸수있음
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일을 읽는것
score_file = open("score.txt", "r" , encoding="utf8")
print(score_file.read())
score_file.close()

#한줄한줄 읽는것
score_file = open("score.txt", "r" , encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 몇줄인지 모를때 방법 1
score_file = open("score.txt", "r" , encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 방법 2
score_file = open("score.txt", "r" , encoding="utf8")
lines = score_file.readline() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()