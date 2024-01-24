
def profile(name, age, main_lang):
    print("이름 : {0} \t나이 : {1} \t주 사용언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 20, "파이썬")

# 위와 같이 같은 정보가 들어갈때 매번일일이 적기 귀찮으므로 함수에 기본값을 지정 해줄수있음

def profile(name, age = 20, main_lang = "파이썬"):
    print("이름 : {0} \t나이 : {1} \t주 사용언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")