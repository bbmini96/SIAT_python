# global
# age = 38 # 전역변수
# def print_age():
#     global age
#     age = 28 # 지역변수
#     print(age)
    
# print_age() # 
# print(age) # 

# nonlocal : 현재 함수 바깥의 지역변수를 변경
# def a():
#     x = 'a'
#     def b():
#         nonlocal x
#         x = 'b'
#     b()
    
#     print(x)

# a()

# 추가)
y = 1000

def a():
    x = 100
    y = 2000
    def b():
        x = 200
        
        def c():
            nonlocal x
            global y      # 전역변수가 없으면 에러 발생
            
            x = x + 300
            y = y + 3000

            print(x) # 500
            print(y) # 에러
        c()
    b()

a()


# closure 클로져
"""
내부 함수가 선언 되었던 환경을 기억하고, 
외부 함수의 밖에서 호출 되더라도 해당 환경에 다시 접근 할수 있는 함수

- 조건
    - 내부 함수
    - 외부 함수의 지역 변수를 참조
    - 외부 함수가 반드시 내부 함수를 return

"""
def outer():
    v = 'value'
    def inner():
        print(v)
    
    return inner
    
result = outer()
result()

# v1
def update_count():
    count = 0
    def plus():
        nonlocal count
        count += 1
        return count
    return plus

result = update_count()
print(result())
print(result())

counter = update_count()
print(counter())