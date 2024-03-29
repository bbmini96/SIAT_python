#import employee as Employee
from employee import Employee

def fetch_data(file_name):
    try:
        emp_list = []
        with open(file_name, 'r') as f:
            lines = f.readlines()    
            
            for line in lines[1:]:
                data = line.strip('\n').split(',') 
                
                eid, ename, job, dept, bonus = data
                
                # print(line.strip('\n').split(','))
                # print(Employee(data[0], data[1], data[2], data[3], data[4]))
                emp_list.append(Employee(eid, ename, job, dept, bonus))
            
        return emp_list
    
    except Exception as e:
        print(e)