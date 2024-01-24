# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
# 일반유니 과 공격유닛의 name 과 hp 가 똑같아서 상속해줄수 있음
# 공격 유닛
class AttackUnit(Unit): # ()괄호안에 상속받고 싶은 클래스 이름을 넣으면 됨
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 클래스 이름 뒤에 . 을찍고 __init__(self, xx, xx) 이렇게 하면 됨
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self. 을 사용을 하면 클래스에 있는 기본값을 사용하고, location 처럼 self. 을 붙이지 않으면 따로 사용을 할수가 있음
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽
# 다중상속
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 5, 67)
valkyrie.fly(valkyrie.name, "3시")

