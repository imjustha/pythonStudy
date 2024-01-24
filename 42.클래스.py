# # 스타크래프트 예제

# # 마린
# name = "marine" #유닛의 이름
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크
# tank_name = "tank"
# tank_hp = 120
# tank_damage = 30

# print("{} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "tank2"
# tank2_hp = 125
# tank2_damage = 23

# print("{} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 :{2}]".format( \
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 이렇게 코드를 짜게 되면 유닛이 늘어날때마다 일일이 적어야 해서 너무 힘듬 그래서 클래스를 사용함

class Unit:
    def __init__(self, name, hp, damage): # init 을 사용하는 이유 : self 를 제외하고 정의된 개수 만큼 값을 줘야함 지금으로 예를 들면 name, hp, damage
                                            #  3개가 있어서 3개를 무조건 적어야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 예를 들어
# marine3 = Unit("마린")
# marine4 = Unit("마린", 40)
# 지금 처럼 개수만큼 정의를 하지않으면 실행이 안됨

# 멤버 변수
# 레이스
wraith1 = Unit("레이스", 70, 20)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # wraith1. 을 찍으면 뒤에 할당하고 싶은 값을 정할수 있음
                                                                        # 멤버변수는 위에 클래스를 사용하지 않고 따로 만들수가 있음
# 마인드 컨트롤, 클로킹
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
# 이처럼 클래스 외부에서 내가 원하는 값을 확장할수도 있고, 확장된 변수는 내가 확장을 한 개체에만 적용이 되고, 기본에 있던 다른 객체에는 적용이 안됨

