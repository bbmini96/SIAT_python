"""
상속
다른 누군가가 만든 기본 형태에 내가 원하는 것만 추가하거나 교체
부모 클래스, 자식 클래스
inheritance(상속): is-a
포함관계: has-a
"""

# 부모 클래스(Parent) 
class Parent:
    p = 'pppppppp'
    __pp = 'pp'
    
    def __init__(self):
        print('p-init')
        self.p_v = 'p_v'
        
    def info(self):
        print('p-info')
        
    def be_rich(self):
        print('p-rich')    
        
        
# 자식 클래스(Customer): class class명(상속받을 클래스 명) 
class Child(Parent):
    c = 'c'
    
    def __init__(self):
        super().__init__()
        print('c-init')
        
    def data(self):
        print('c-data')
        
    def be_rich(self):
        super().be_rich()
        print('c-rich')
        


# BookingList(포함) - Customer 내부의 변수로 활용        

        
# child = Child()
# child.info()    # 상속

# Parent + __init__   # 자식에 init이 없으면 가능
# child2 = Child()    # -> p-init: 자식 객체는 부모 객체가 있어야만 함

# Child + __init__
# child2 = Child()

# Error 자식에 init이 있으면 부모의 인스턴스를 가져오지 못한다
# super() 키워드 사용하면 해결 가능
# super(): 상속을 해준 부모 클래스를 의미한다
# child_init 내부에서 부모의 init 메소드 호출
# super().__init__()
# print(child2.p_v)   
# print(child2.p) 



# Parenet + def be_rich
# Child   + def be_rich
# 오버라이딩 => 메소드 이름, 파라미터가 똑같으면
# 자식의 것만 호출된다
# child3 = Child()
# child3.be_rich()



# 부모의 private 변수/메소드 상속 불가능!
# print(child.__pp)

# 클래스가 상속 관계인지 확인: issubclass(자식클래스, 부모클래스) => True,False만 사용
# print(issubclass(Parent, Child))

# 관계 없는 클래스 상속 확인
# class A:
#     pass
# class B:
#     pass
# print(issubclass(Parent,A))

"""
class Customer():
    def __init__(self,id,name,credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
    
    def get_credit(self):
        return self.__credit
    
    def __str__(self):
        return f'id: {self.__id}, name: {self.__name}, credit: {self.__credit}'
     
     
class VIPCustomer(Customer):
    __grade = 'VIP'
    def __init__(self,id,name,credit):
        super().__init__(id,name,credit)
    
    def get_credit(self):
        return super().get_credit() * 1.5
    
    def __str__(self):
        return super().__str__() + f', Grade: {self.__grade}, {VIPCustomer.get_credit(self)}'
    
         
class GoldCustomer(Customer):
    __grade = 'Gold'
    def __init__(self,id,name,credit):
        super().__init__(id,name,credit)
    
    def get_credit(self):
        return super().get_credit() * 1.3 
    
    def __str__(self):
        return super().__str__() + f', Grade: {self.__grade}'   
        
        
class SilverCustomer(Customer):
    __grade = 'Silver'
    def __init__(self,id,name,credit):
        super().__init__(id,name,credit)

    def get_credit(self):
        return super().get_credit() * 1.2
    
    def __str__(self):
        return super().__str__() + f', Grade: {self.__grade}'
        
        
class BronzeCustomer(Customer):
    __grade = 'Bronze'
    def __init__(self,id,name,credit):
        super().__init__(id,name,credit)
    
    def get_credit(self):
        return super().get_credit() * 1.1
    
    def __str__(self):
        return super().__str__() + f', Grade: {self.__grade}'


vipCu = VIPCustomer('1213','ddv',1000)
goldCu = GoldCustomer('1213','ddg',1000)
silverCu = SilverCustomer('1213','dds',1000)

print(vipCu)
print(goldCu)
print(silverCu)
"""


# 추가) 다중 상속

# class University:
#     def print_info(self):
#         print('대학교입니다')
        
# class Institure:
#     def print_info(self):
#         print('학원입니다')
        
# class Student(University, Institure):   # 다이아몬드 상속
#     def print_info(self):
#         print('학생입니다')

# student = Student()
# student.print_info()  # 오버라이딩으로 인해 학생입니다가 출력

# # mro() => 메소드 탐색 순서
# print(Student.mro())    # 상속받을때 먼저 선택한 것을 참조한다


# 추상클래스(Abstract class) 상속받는 클래스가 반드시 지정된 메소드를 구현해야 한다고 강제

from abc import *

# class Base(metaclass = ABCMeta):
#     @abstractmethod
#     def write_introduce(self):
#         pass

# class JobHunter(Base):
#     def write_introduce(self):
#         print('자소서 완료')

# jack = JobHunter()
# print(jack)
# jack.write_introduce()


class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_doc(self):
        pass

    @abstractmethod 
    def cancel_doc(self):
        pass

class SMPrint(Print):
    def print_doc(self):
        print('성민프린터')

    def cancel_doc(self):
        print('성민프린터')

class HJPrint(Print):
    def print_doc(self):
        print('혜진프린터')

    def cancel_doc(self):
        print('혜진프린터')

sm = SMPrint()
hj = HJPrint()

sm.print_doc()
hj.print_doc()


print = Print()
print.print_doc()


# 추상 클래스 사용 이유
# 꼭 필요한 기능 정의를 자식 클래스에서 지정하기 위해

# 추상 클래스 사용 문법
# from abc, metaclass, @abstractmethod

# 추상 클래스 주의
# 추상클래스는 자체적으로 객체 생성 불가능 : 완전한 메소드가 X
 
        
        
        
        
        
        
        
        
        
        
        
        
        