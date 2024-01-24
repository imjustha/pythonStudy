import pickle
# 쓰기 전용

profile_file = open("profile.pickle", "wb") # w를 적어주고, b를 항상 적어줌(binary 라는 뜻)
profile = {"이름" : "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

# 저장된 파일 불러오기
profile_file = open("profile.pickle", "rb")  # r을 적어줌
profile = pickle.load(profile_file)   # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
