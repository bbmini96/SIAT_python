"""
리스트, 튜플, 딕셔너리, 셋

1. 리스트 : 순서, 중복, 수정, 삭제
- 가장 많이 사용하는 시퀀스 자료형
- 선언 : list(), []
- 종류
    - 기본 리스트
    - 혼합형 리스트 : 다양한 자료형
    - 매트릭스 리스트 : 매트릭스 구조
- 인덱싱, 슬라이싱
- 정렬: 리스트.sort()=>오름차순
- 삽입: append(한개 요소), insert(위치,한개 요소),extend(한번에 여러요소 추가)
- 수정: 해당 위치의 요소값 변경,
- 삭제: del(리스트[인덱스]), 리스트.pop(인덱스), 리스트.remove(요소), 리스트.clear()
"""
list1 = [1,2,3]
list2 = list(range(4,7))
# print(list2, type(list2))
# list3 = [1,2,3,[4,5,6,[7,8,9]]]
# print(list3, type(list3))
# list4 = ["안녕",'안','녕']
# print(list4, type(list4))
# list1.extend([3,4,5,6])
# print(list1)
# =============================================================

# 조회(count(요소) => 요소의 개수 반환), index(요소) => 위치값 반환
list3 = [1,2,3,4,5]
# print(list3.index(4))
# =============================================================

# 정렬 sort()오름차순, reverse(), sort(reverse=True) 내림차순
list4 =[123,3,56,78,90,314,4,5,6,1324,565]
# list4.reverse()
# print(list4)
# list4.sort(reverse=True)
# print(list4)

list5 = ["D",'b','c',"A"];
list5.sort(key=str.upper, reverse=True);
# print(list5);

list6 = [True,False,56,1,3]
list6.sort()
# print(list6)

# min,max,sum

# print(min(list4))
# =============================================================

# enumerate
snacks = ['오도독', '알새우칩', '오징어땅콩', '몽셀']

# for i in enumerate(snacks):
    # print(i)
# =============================================================

# list comprehenction(이해): 파이썬의 리스트를 함축적으로 표현하는 식
numbers = []

numbers = [i for i in range(1,11)]
# print(numbers)
# =============================================================

# 짝수만 표현
even_numbers = [i for i in range(1,11) if(i %2 == 0)]
# print(even_numbers)
# =============================================================

# list = [[1,2,3],[4,5,6],[7,8,9]]
one_list = []

# for i in range(len(list)):
#     for j in range(len(list)):
#         one_list.append(list[i][j])

# print(one_list)


# one_list = [j for i in list for j in i ]
# print(one_list)
# =============================================================

fruits = ['apple','banana','cherry','dottory']
list_fru =[]

for i in fruits:
    list_fru.append(i.upper())
    
# print(list_fru)

# print([i.upper() for i in fruits])

# =============================================================

import time;

# 1 ~ 1000000
start_time = time.time()

# v1
numbers = []
# for i in range(1, 1000001):
#     numbers.append(i)
    
# end_time = time.time()

# print('for ~ range : ', end_time - start_time)
# =============================================================

# v2
numbers = [i for i in range(1, 1000001)]

end_time = time.time()

# print('for ~ range : ', end_time - start_time)
# =============================================================

# 깊은 복사, 얕은 복사
origin_list = [1,2,3];
copy_list = origin_list;

# 얕은 복사
# is는 파이썬에서 같은 객체인지 판별
# print(origin_list is copy_list);

copy_list[1] = 20
# print(origin_list is copy_list);

origin_list = [[1,2],[3,4]];
copy_list = origin_list;

copy_list[1].append(5)
# print(copy_list)
# print(origin_list)

#===============================================================

# 깊은 복사



deep_list = origin_list.copy()
deep_list[1] = 10
# print(origin_list is deep_list)

import copy
origin_list = [[1,2],[3,4]];

# copy_list = copy.deepcopy(origin_list);

# copy_list[1].append(5)
# print(copy_list)
# print(origin_list)

copy_list = []

copy_list = [copy_list[:] for copy_list in origin_list]

copy_list[1].append(5)
# print(copy_list)
# print(origin_list)
#===============================================================

# map: 내부적으로 가져온다음 새로운 나열된 객체를 만들어 준다
# map(type, 리스트?)
float_list = [1.2, 3.4, 4.5]

float_list = list(map(int, float_list))
# print(float_list)




    


"""
2. 튜플 : 순서, 중복
- 값을 변경할 수 없는 자료형
- 선언 : (), 나열
- 인덱싱, 슬라이싱
"""

tuple1= (1,2,3,4,5);
# print(tuple1);

v1,v2,v3,v4,v5 = tuple1;
# print(v1,v2,v3,v4,v5)
#===============================================================

snacks = ['오도독', '알새우칩', '오징어땅콩', '몽셀']

# for idx, element in enumerate(snacks):
    # print(f'idx: {idx}, value: {element}')
#===============================================================

tuple2 = tuple((6,7,8,9))
# print(tuple2);
#===============================================================

tuple3 = tuple(i for i in range(1,11) if i % 2 == 0)
# print(tuple3);
#===============================================================

tuple4 = tuple(map(int, float_list))
# print(tuple4);




"""
3. 딕셔너리 : 수정, 삭제
- {key1 : value1, key2 : value2, ...}로 선언되어 키로 지정 값을 리턴하는 자료형
- 딕셔너리는 순서가 없음
- key는 중복이 없음
- 반환, 삽입
"""

dic1 = {'name': 'it', 'age': 28}
# print(dic1)
#===============================================================

# 조회 ['key'], get('key'), 딕셔너리.value(), 딕셔너리.keys(), 딕셔너리.items()
# print(dic1['name']);      => Error
# print(dic1.get('a'));     => None


dic2 = {1:'one',2:'two'}   # 사용은 가능하나 문자열로 표현한다
# print(dic2[1])
#===============================================================

dic3 = dict({'skill':'back'})
# print(dic3)
#===============================================================

# zip: 하나씩 담아서 tuple로 반환한다
a = [1,2,3]
b = [4,5,6]

zipped = zip(a, b)
# print(dict(zipped))
#===============================================================

a1 = ['name','age']
b1 = ['it', 28]

# print(dict(zip(a1,b1)))

#===============================================================

# 추가
dev = {'name': 'front', 'age': 28};

dev['skill'] = 'JavaScript';
# dev['dept'] = None;
#===============================================================

dev.setdefault('dept')  # setdefault는 키만 추가한다
#===============================================================

# 수정 (update(key = 'value')) => key가 문자열일 때만 작동한다
# dev['skill'] = 'react.js';
dev.update(skill = 'react.js')
# print(dev);
#===============================================================

# 삭제 pop('key'), del 딕셔너리['key'], 딕셔너리.clear()
dev.pop('age')
# print(dev);

# print(dev.values())
# print(dev.keys())
# print(dev.items())

# for key,value in dev.items():
    # print(f'key: {key}, value: {value}')
#===============================================================


# fromkeys (키 값을 갖고 있는 반복 객체(list, tuple), default, value)

keys = ['color', 'capacity', 'price']

# cell_phone = dict.fromkeys(keys, 100)
# print(cell_phone)

cell_phone = {key:value for key, value in dict.fromkeys(keys).items()}
# print(cell_phone)



brand = ['mega','venti','sbuk']

coffee_brand = dict.fromkeys(brand,100)
# print(coffee_brand)

coffee_br = copy.deepcopy(coffee_brand)

coffee_br['mega'] = 1000;
# print(coffee_br)
# print(coffee_brand)

    
    

"""
4. 셋
- 중복되지 않은 요소들의 집합
- 선언
- 집합
"""
fruits = {'grape','orange','berry','orange'}
# print(fruits)

# number_set = set([5,2,7,2,6,8,6,3,1])
# print(number_set)

# str_set1 ={'abc'}
# str_set2 =set('abc')

# print(str_set1)
# print(str_set2)

# str_set = {str_set1,str_set2}
# print(str_set)


prac_set = {1, 2, 3, 4, 5}

# in 연사자로 조회하기
# print(6 in prac_set)
# print(3 in [1,2,3])
# print(3 in {1,2,3})
# print(6 in {6: 'six', 'six':6})


# 추가: add, update(튜플을 사용시 두개이상의 리터러블값이 있어야한다)
# prac_set.add(6)
# print(prac_set)
# prac_set.update([7])
# print(prac_set)
# prac_set.update((8,9))
# print(prac_set)
# prac_set.update({10})
# print(prac_set)



# 삭제: remove, discard
# prac_set.remove(5)    # 없는 값을 넣으면 key Error
prac_set.discard(10)    # Error가 안난다
# print(prac_set)

# 집합특성
feature_set1 = set([0, 1, 2, 3, 4, 5]) 
feature_set2 = set([4, 5, 6, 7, 8, 9])

# 합집합(union, or)
# print(feature_set1.union(feature_set2))
# print(feature_set1 | feature_set2)


# 차집합(defference, -)
# print(feature_set1.difference(feature_set2))
# print(feature_set1 - feature_set2)

# 교집합(intersection, &)
# print(feature_set1.intersection(feature_set2))
# print(feature_set1 & feature_set2)

# 부분집합(issubset, issuperset, >)
sub_set = set([1,2])
super_set = set([1,2,3,4])

# print(sub_set.issubset(super_set))
# print(sub_set > super_set)

# isthisjoint 연결 점이 있나 없나
# print(super_set.isdisjoint(sub_set))











"""실습
1) 중복 수강 학생 파악하기
- Economy와 Biology를 수강하는 학생 목록을 보고 중복 수강 학생을 추려내기
"""

economy = {'Adela', 'Grania', 'Ava', 'Fred', 'Bianca', 'Dana', 'Emma', 'Mary', 'Jim', 'Clara'}
biology = {'Elijah', 'Emma', 'Liam', 'Sophia', 'Olivia', 'Isabella', 'Grania', 'Sally', 'Peter', 'Fred'}

name = []

# for i in economy:
#     for j in biology:
#         if i == j:
#             name.append(j)
            
# print(name)

# print([j for i in economy for j in biology if(i==j)])
# print(economy.intersection(biology))



"""
2) 파일 골라내기
- 실행파일(확장자명 : pdf) 파일만 골라내기
"""
files = ['coffee.jpg', 'food.pdf', 'medicine.txt', 'customer.hwp', 'puppy.pdf', 'plant.jpg']
# files_pdf = []

# for i in files:
#     if ".pdf" in i:
#         files_pdf.append(i)
        
# print(files_pdf)
     

# print([files_pdf for files_pdf in files if ".pdf" in files_pdf])
# print([files_pdf for files_pdf in files if ".pdf" in files_pdf])

from functools import reduce

# def files_pdf_f(files_pdf):
#     for i in files:
#         if ".pdf" in i:
#             files_pdf.append(i)
#     return files_pdf

# print(list(filter(lambda file : file.split('.')[-1] == 'pdf', files)))
# print(list(filter(lambda file : file.find('.pdf') != -1, files)))



