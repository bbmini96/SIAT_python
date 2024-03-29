"""
Class 클래스
 - 생성자 def __init__(self)
"""

class User:
    # 생성자
    def __init__(self, name, age):     # 매직메소드
    #     print('user 생성자')
        self.name = name
        self.age = age
        # private 변수
        self.__age = age
        
    # def __init__(self,*args):
        # self.name = args[0]
        # self.age = args[1]
    # def __init__(self,**keyword):
    #     # 인스턴스 변수
    #     self.name = keyword['name']
    #     self.age = keyword['age']
     
        
    # name 반환하는 메소드 getName
    def getName(self):
        return self.name
    
    # getAge
    def getAge(self):
        return self.__age 
    
    # setAge
    def setAge(self, age):
        self.__age = age
    
    # __str__
    def __str__(self):
        return '__str__'
    
    
        
# first_user = User()
# print(first_user)

dev = User('it',28)
# print(dev.name)
# print(dev.age)
# print(dev.getName())

# 존재하지 않는 속성을 추가하는 방법
dev.skill = 'python'
# print(dev.__dict__)     # parameter


gamer = User('gamer',30)
# print(gamer.age)
# print(gamer.getAge())

gamer.__age = 80 # 변경 불가능
# print(gamer.getAge())

gamer.setAge(80)
# print(gamer.getAge())

# Customer 고객 객체 
# id, grade, nick_name
# id는 private 변수
# grade, nick_name -> getter, setter
class Customer:
    def __init__(self, id, grade, nick_name):
        self.id = id
        self.grade = grade
        self.nick_name = nick_name
        
    def get_id(self):
        return self.id
    
    def get_grade(self):
        return self.grade
    
    def get_nick_name(self):
        return self.nick_name
    
    def set_grade(self, grade):
        self.grade = grade
        
    def set_nick_name(self, nick_name):
        self.nick_name = nick_name



class Student:
    
    # __slots__ = ['attribute','attr',....]
    __slots__ = ['name', '__age','score']
    
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age        # 프리이빗 객체
        
    # def __str__(self):
    #     return f'name: {self.name}, age: {self.__age}'

    def __repr__(self):
        return str(self.name) 
    
    # __add__,__sub__, __mul__, __div__: +, -, *, /
    # __eq__, __ne__, __gt__, __lt__: ==, !=, >, <
    def __add__(self, other):
        return self.__age + other.__age
    
    # __del__ : 인스턴스 삭제
    # def __del__(self):
    #     print(f'해당 객체{self.name} 삭제')
    
    
      
     
jack = Student('jack',28)
jack.score = 100

cindy = Student('cindy',28)
cindy.score = 90

# __dict__: 해당 객체가 가지고 있는 속성 키와 값을 딕셔너리로 알려준다
#           __slots__을 사용하면 __dict__ 사라진다
# print(jack.__dict__)
# print(cindy.__dict__)

# dir() 기능을 이용해 객체가 갖고 있는 모든 정보 출력
# __slots__ 사용시 dict대신 사용할 수 있음
# print(dir(jack))
# print(dir(cindy))




# print(dir(jack))
# print(dir(cindy))

# __repr__: 객체의 정보를 출력


# print(jack)
# print(cindy)

# print(jack + cindy)
