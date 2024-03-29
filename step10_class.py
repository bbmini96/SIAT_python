class Developer:
    # 모든 클래스 들이 사용할 수 있는 클래스 변수
    skills = []
    __max_sal = 100
    
    
    # 인스턴스 메소드
    def __init__(self, name):
        self.name = name        # 인스턴스 변수
        # self.skills = []
        
    # 인스턴스 메소드
    def add_skills(self,skill):
        self.skills.append(skill)
        
        
    # 클래스 메소드 
    # @staticmethod
    @staticmethod
    def print_info(sal):
        print('--@static--')
        print(sal)
        # print(skills) # NameError
        # print(__max_sal) # NameError
    
    
    # 클래스 메소드     
    # @classmethod(cls, ...)
    @classmethod
    def print_param(cls, param):
        print('--@class--')
        print(param)
        print(cls.skills)
        print(cls.__max_sal)
        
        
        

# front,back 기술들을 객체 추가 -> skill        
front_dev = Developer('front')

front_dev.add_skills('js')
front_dev.add_skills('react.js')


back_dev = Developer('back')

back_dev.add_skills('spring')
back_dev.add_skills('JPA')



# Developer.print_info(100)           # 클래스 메소드
# Developer.add_skills('spring')      # 인스턴스 메소드
# Developer.print_param(100)


# 클래스 메소드 @static vs @class
# 클래스 변수       X   vs   O
# 사용 : 클래스 변수에 접근할 필요성이 있다면 @classmehtod 사용할 것!
Developer.print_info('@static')
Developer.print_param('@class')









method_set = {1,2,3}

method_set.update({4})
# print(method_set)


# print(set.union({1,2,3},{4}))


