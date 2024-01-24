# 출석번가 1,2,3,4 엎에 100을 붙이기로함 -> 101,102,103,104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생이름을 길이로 변환
student = ["iron man", "thor", "groot"]
student = [len(i) for i in student]
print(student)

#학생 이름을 대문자로 변환
student = ["iron man", "thor", "groot"]
student = [i.upper() for i in student]
print(student)