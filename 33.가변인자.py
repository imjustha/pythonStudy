def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0} \t나이 : {1}\t".format(name, age), end=" ") # 뒤에 end= " " 를 사용하면 줄바꿈없이 됨
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 25, "kotlin", "swift", "", "", "")

# 위와 같이 매번 새로운 정보들이 추가되면 일일이 넣기 힘들기 때문에 가변인자를 사용해줌

def profile(name, age, *language):
    print("이름 : {0} \t나이 : {1}\t".format(name, age), end=" ") # 뒤에 end= " " 를 사용하면 줄바꿈없이 됨
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "kotlin", "swift")