

line_list = []
with open('employees.csv','r',encoding='UTF-8') as fi:
    for line in fi.readlines()[1:]:
        line_list.append(line.strip('\n').split(','))  
            

class Emplyee:
    def __init__(self,eid,ename,job,dept,bonus):
        self.eid = eid
        self.ename = ename
        self.job = job
        self.dept = dept
        self.bonus = bonus

    
    def __str__(self):
        return f'eid: {self.eid}, name: {self.ename}, job: {self.job}, dept: {self.dept}, bonus: {self.bonus}'

emplyee_list = []
bonus_list = []

for i in range(len(line_list)):
    if line_list[i][4] == 'None':
        bonus_list.append(int('0'))
    else:
        bonus_list.append(int(line_list[i][4]))
    emplyee_list.append([line_list[i][0],line_list[i][1],line_list[i][2],line_list[i][3],bonus_list[i]])
    emplyee_list = sorted(emplyee_list, key= lambda x: x[-1])

    
# print(line_list)
def emplyee_f():
    for i in range(len(line_list)):
        emplyee = Emplyee(emplyee_list[i][0],emplyee_list[i][1],emplyee_list[i][2],emplyee_list[i][3],emplyee_list[i][4])
        print(emplyee)
        
# emplyee_f()


#=======================================================================
# def open_emp():
#     try:
#         line_list = []
#         with open('employees.csv','r',encoding='UTF-8') as fi:
#             lines = fi.readlines()
#             for line in lines[1:]:
#                 data = line.strip('\n').split(',')
                
#                 eid, ename, job, dept, bonus = data
#                 line_list.append(Emplyee(eid, ename, job, dept, bonus))
                
#             return line_list  
          
#     except Exception as e:
#         print(e)
    
          

# class Emplyee:
#     def __init__(self,eid,ename,job,dept,bonus):
#         self.eid = eid
#         self.ename = ename
#         self.job = job
#         self.dept = dept
#         self.bonus = bonus

    
#     def __str__(self):
#         return f'eid: {self.eid}, name: {self.ename}, job: {self.job}, dept: {self.dept}, bonus: {self.bonus}'

# emplyee_list = []
# bonus_list = []

# for i in range(len(line_list)):
#     if line_list[i][4] == 'None':
#         bonus_list.append(int('0'))
#     else:
#         bonus_list.append(int(line_list[i][4]))
#     emplyee_list.append([line_list[i][0],line_list[i][1],line_list[i][2],line_list[i][3],bonus_list[i]])
#     emplyee_list = sorted(emplyee_list, key= lambda x: x[-1])

# def emplyee_f():
#     for i in range(len(line_list)):
#         emplyee = Emplyee(emplyee_list[i][0],emplyee_list[i][1],emplyee_list[i][2],emplyee_list[i][3],emplyee_list[i][4])
#         print(emplyee)
        
# emplyee_f()

# ==============================================================================

import fetch

def show_data(data_list):
    for data in data_list:
        print(data)
        
if __name__ == '__main__':
    data_list = fetch.fetch_data('employees.csv')
    fetch.show_data(data_list)

def sort_eid(data_list, mode):
    mode = mode
    for data in sorted(data_list, key=lambda emp:((emp.get_bonus()=='None') and -1), reverse=mode):
        print(data)

sort_eid(data_list, False)


    



      
        