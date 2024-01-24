# pickle 을 사용하는 경우

# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with 를 사용하면 close 를 해줄 필요없음

# pickle 을 사용하지 않는 경우

with open("study.txt", "w", encoding="utf8") as study_file: # utf8을 사용하면 한국어를 볼수있음
    study_file.write("저는 파이썬을 공부중입니다")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())