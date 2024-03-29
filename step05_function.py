"""
함수(Function)

- 특정한 명령을 수행하는 하나의 독립된 프로그램
- 객체로 관리됨
- 반복 코드를 줄여 간단하게 만들 수 있음
- 라이브러리 함수, 사용자 정의 함수, 기본 함수
- 정의
> def 함수명('매개변수'):
            명령문
- 호출 : 함수명()
"""
# def print_str(str):
#     # print(str)
#     return str
    
# print_str('Hellow')


"""
매개 변수가 있는 함수

- 매개변수(Parameter) : 호출 함수에 초기값을 대입할 변수
- 인수(Argument) : 호출할 때 전달 할 값
"""



"""1. 기본 인수"""
def print_product(item, count):
    print(item, count)
    
# print_product('coffee', 20)




"""2. 가변 인수

- *args  => 리턴 타입: 튜플(args는 바꿀 수 있지만, * = 가변인수)
"""
# def print_item(*params):
    # print (params);

# print_item('age', 'bread', 'beer');




"""3. 키워드 인수

- **kwargs  => 리턴 타입: 딕셔너리(key = value)
"""
# def print_food(**kwargs):
#     print(kwargs)

# print_food(dinner = "soup")

# menu: 'kimchi soup', 주문수량(count): 3, 최종가격(price): 30000

# def print_food(**kwargs):
#     # print('메뉴명:{}, 주문수량:{},가격:{}'.format(kwargs['menu'],kwargs['count'],kwargs['price']))
#     print(f'메뉴명:{kwargs["menu"]}, 주문수량:{kwargs["count"]}, 가격:{kwargs["price"]}')
    

# print_food(menu = "Kimchi soup", count = 3, price = 30000)


# 1) [1, 2, 3], [3, 1, 4] 두개의 리스트 -> 값이 다른 것을 짝을 지어 출력
# 예상 결과)[(1,3),(1,4),(2,3),(2,1),(2,4),(3,1),(3,4)]
list1 = [1,2,3]
list2 = [3,1,4]
list3 = []

for i in list1:
    for j in list2:
        if i != j:
            list3.append(tuple((i,j)))

# print(list3)

# print([(i,tuple_list) for i in list1 for tuple_list in list2 if i != tuple_list])


# 2) 각 도시와 음절 수 출력
# 예상 결과)[('seoul':5)]
city= ['seoul','osaka','deli','beijing']
count_list = []


for i in city:
    count_list.append(tuple((i,len(i))))
    
# print(count_list)

# print([(i,len(i)) for i in city]) 





""" 여러 인자를 넘겨받는 함수 선언
- 순서 : 일반 인자, 가변 인자, 키워드 인자
"""



""" 4. 람다 함수
- 이름이 없는 익명함수로 lambda로 명명
- 한 줄로 간단히 정리 할 수 있는 함수
- lambda 파라미터: 반환값
"""

plus = lambda x, y: x+y 
# print(plus(5,10))

# 즉시 실행
# (lambda x, y: print(x + y))(5,10)
# (lambda x, y=10: print(x + y))(5)




""" filter()
1. filter(함수, 리스트)
2. 리스트의 값을 함수에 인수로 전달하여 조건에 맞는 결과 값을 리스트로 반환
"""
def even(element):
    return element % 2 == 0


# print(list(filter(even, range(1,21))))
# print(list(filter(lambda element: element % 2 == 0, range(1,21))))




""" map()
1. map(함수, 리스트)
2. 시퀀스 자료형 각 요소를 함수에 인수로 전달하여 출력되는 값을 리스트로 반환
"""
map_list = [1, 2, 3]
# map_list의 각 원소를 제곱한 원소값을 값는 리스트를 반환
def power(element):
    
    return element*element
# print(list(map(power,map_list)))
# print(list(map(lambda element: element*element, map_list)))

a_list = [1, 2, 3, 4, 5]
b_list = [10, 20, 30, 40, 50]

# print([a_list[i]+b_list[i] for i in range(5)])

# print(list(map(sum, zip(a_list,b_list))))

# print(list(map(lambda a,b: a + b, a_list,b_list)))


""" reduce()
1.reduce(함수, 시퀀스)
2.시퀀스 나열 항목 순서대로 함수에 인수로 전달, 출력 되는 값을 계속 인수로 전달 및 연산 하여 그 결과를 리스트로 반환

"""
# 1 ~ 10
from functools import reduce

# print(reduce(lambda x ,y : x + y, range(1,11)))




# sort
# burgers = [('Mc', 35, 3040),('Bk', 40, 1300),('MomS', 10, 200)]

# print(burgers)
# burgers.sort(key=lambda x: x[1])
# print(burgers)


# 딕셔너리 리스트 정렬
burgers =[
    {'name' : 'Mc', 'gram' : 35, 'kcal' : 3040},
    
    {'name' : 'Bk', 'gram' : 40,'kcal' : 1300},
    
    {'gram' : 10, 'name' : 'MomS', 'kcal' : 200}
]

# dic_MC = {
#     'name' : 'Mc', 
#     'gram' : 35, 
#     'kcal' : 3040
#     }

# dic_BK = {
#     'name' : 'Bk', 
#     'gram' : 40,
#     'kcal' : 1300
#     }

# dic_MomS = {
#     'name' : 'MomS', 
#     'gram' : 10, 
#     'kcal' : 200
#     }

# burgers = [dic_MC, dic_BK, dic_MomS]
# print(sorted(burgers, key=lambda x: x['gram']))  


# print([dict(sorted(buger.items(), key=lambda item: item[0])) for buger in burgers])
 


# burgers.sort(key = lambda x: x['kcal'])

# from operator import itemgetter

# print(sorted(burgers, key=itemgetter('gram')))

# print(burgers)


# 키 정렬 기초
alpha_dict = {'d': 4, 'a': 1, 'b':2, 'c':3}
# 키 기준 정렬
print(dict(sorted(alpha_dict.items(), key=lambda x: x[0])))

# 벨류 기준정렬
print(dict(sorted(alpha_dict.items(), key=lambda x: x[1])))







"""재귀함수"""
# factorial(n)
# 1 -> 1, 2 -> 2*1, 3 -> 3*2*1

# def factorial(n):
    
#     if n ==0:
#         return 1;
#     else:
#         return n * factorial(n-1)

# print(factorial(4))


# 피보나치 수열
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

# cnt = 0
# def fibonacci1(n):
#     global cnt
#     cnt += 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
    
#     return fibonacci1(n-1) + fibonacci1(n-2)

# print(fibonacci1(10))
# print(f'fibonacci(10): {cnt}')


# 메모화(memoiztion)
# 메모 변수를 만들어 준다

# memo = {
#     1 : 1,
#     2 : 1
# }

# cnt1 = 0
# def fibonacci(n):
#     global cnt1
#     cnt1 += 1
#     if n in memo:
#         return memo[n]  
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#         memo[n] = result
#         return result
    
# print(fibonacci(10))