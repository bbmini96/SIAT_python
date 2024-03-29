# Employee 클래스 생성
class Employee:
    
    def __init__(self, eid, ename, job, dept, bonus):
        self.__eid = eid
        self.__ename = ename
        self.__job = job
        self.__dept = dept
        self.__bonus = bonus
        
    def get_eid(self):
        return self.__eid
    
    def get_bonus(self):
        return self.__bonus
        
    def __str__(self):
        return f'eid : {self.__eid}, name : {self.__ename}, job : {self.__job}, dept : {self.__dept}, bonus : {self.__bonus}'
 