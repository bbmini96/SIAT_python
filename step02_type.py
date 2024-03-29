"""
[자료형]

자료가 가지는 형으로 구조와 값으로 구성
- type으로 확인 가능
"""



""" 1. 불리언(Boolean)
- 참(True), 거짓(False)
- 논리(and, or, not)
- 비교(==, !=, <, <=, >, >=)
"""

""" 2. 숫자
- 실수(float), 정수(int)
- 복소수(complex) => j로 표현
- 연산(+, -, *, /)
- 몫(//), 나머지(%), 제곱(**)
"""
#formmating
# %s-문자열, %d-정수, %f-실수
# print("%s %d %0.1f" %('n', 3, 2.56))  # %0.자리수f, 반올림한다 

# format()
# '{}'.format()
# print("I like {} and {}".format('Pizza','Rice'))
# 인덱스 번호 지정
# print("I like {0} and {0}".format('Pizza','Rice'))


""" 3. 문자열(String)
- 선언("" or '' 로 감싸어 선언)
- 형변환(str())
- 길이(len)
- 인덱싱(indexing), 슬라이싱(slicing)
- 이스케이프(escape) 코드(\n, \t, \r, ..)
- 다중 인용부호(''' or ''')
- 함수
> lower(), upper(), find(), strip(), replace(), split(), count()
"""




""" 문자열 문제
1. 휴대폰 번호에서 숫자만 출력하기
"""
cell = "010-1234-5678"
# print(cell.replace('-',''));



"""
2. 해당 경로에서 파일명만 출력하기
"""
path = "C:\Program Files\Internet Explorer\iexplore.exe"
# print(path.split("\\")[3]);

# raw string: r => 특수기호도 출력시켜준다
# print(r"C:\Program Files\Internet Explorer\iexplore.exe");



# 선언
str1 = 'Hellow,Python';
# print(type(str1));
# print(str1 + ":)");
# print(str1 * 3)

# 인덱싱 : 변수명[idx] - 양수,음수 모두 인덱싱 가능하다
# print(str1[-3]);

# 길이: len()
# print(len(str1));

# 슬라이싱: 변수명[시작:끝:단계]
# print(str1[0:2])
# print(str1[3:])
# print(str1[3::2]);
#print(str1[13::-1]); # 역순으로 나온다

str_fn = "happy smile shine";

# find 
# print(str_fn.find('i'));

# upper/lower
# print(str_fn.upper());

# replace(old, new) 변경하는 함수 old에서 new로 변경한다

# count
# print(str_fn.count('e'));

# split(): 아무것도 지정안하면 띄어쓰기를 기준으로 잘라준다
# print(str_fn.split());

# strip(): 양쪽 끝 빈공간들만 제거
str_strip = ' bread, ramen '
# print(str_strip.strip());

# sep seperate 분리하다 기준으로
# end 문자열 끝에 출력 시키고 싶은 문자
# print("N","E",'W', sep="", end="!");


# f-string
# f'{데이터}'
menu = 'coffee';
count = 3;
result = f'menu: {{{menu}}}, count:{count}'
print(result)

# 맨뒤의 2개 문자 출력
print(f'맨뒤의 2개 문자 출력{menu[-2:]}')

print(f'menu = {menu}')
print(f'{menu = }') # coffee의 값이 ''안에 나옴


# 정렬
str2 = 'right';
print(f'|{str2:>10}|'); # 오른쪽정렬 >
print(f'|{str2:<10}|'); # 왼쪽정렬 <
print(f'|{str2:^10}|'); # 가운데정렬 ^


# isdecimal(): 문자열이 정수 형태인지 확인
# isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인, (음수X,실수X,분수X)
# isnumeric(): 문자열이 숫자로 인식될 수 있는 것인지 확인, (음수X,실수X,분수O)
decimal_str = '12345';
float_str = '12.345';

print(decimal_str.isdecimal()); #True
print(decimal_str.isdigit());   #True
print(float_str.isdecimal());   #False
print(float_str.isdigit());     #False  .이 숫자로 인식하지 못한다
print(float_str.isnumeric())    #Fasle
