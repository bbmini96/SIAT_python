"""
제어문

1. 조건문
2. 반복문
"""

"""
1. 조건문
- 주어진 조건을 비교하여 참, 거짓에 따라 명령 제어
- 관계 연산자(<, <=, >, >=, ==, !=), 논리연산자(and, or, not)
- 단일 및 다중 조건(if ~ elif, else)
- 중첩 조건

- 기본 문법
if 조건:
    명령
"""



""" 조건문 실습
1) 신용평가 등급 판별하기
> 점수에 따른 신용평가 등급
- A+ : 95점 이상
- A : 90점 이상
- B+ : 85점 이상
- B : 80점 이상
- C : 80점 미만
"""
# score = 30;
# if score < 80:
#     print('C등급입니다.');
# elif score < 85:
#     print('B등급입니다.');
# elif score < 90:
#     print('B+등급입니다.');
# elif score < 95:
#     print('A등급입니다.');
# else:
#     print('A+등급입니다.');


    




"""
2) 양수, 음수 판별하기
- 양수, 음수 판별하기
- 0도 구별할 것
"""
# num1 = 3;
# if num1 < 0:
#     print('음수입니다.');
# elif num1 > 0:
#     print('양수입니다.');
# else:
#     print('0입니다.');



""" 
3) 지원 분류 프로그램
- 경력과 성적에 따른 지원 분류 프로그램

- 5년 이상 경력만 지원 가능
- 100점 만점 90점 이상은 A부서, 80점 이상은 B부서, 그 외 지원불가
"""
# num2 = 4;
# num3 = 70;
# if num2 > 4:
#     if num3 > 80:
#         print("당신의 부서는 B부서입니다.");
#     elif 89< num3 <101 :
#         print("당신의 부서는 A부서입니다.") ; 
#     else:
#         print("지원불가 입니다.")
# else:
#     print("5년이상 경력만 지원 가능합니다.");


""" 
4) 성별 구분하는 프로그램
- 주어진 주민번호 뒷자리 7자리를 이용하여 남,여 구분하는 프로그램

- 1, 3으로 시작하면 남성
- 2, 4로 시작하면 여성
"""

# num4 = 4234567;
# if str(num4)[0] == 1 or str(num4)[0] == 3:
#     print("남성입니다");
# elif str(num4)[0] == 2 or str(num4)[0] == 4:
#     print("여성입니다");
# else:
#     print("주민번호가 잘못입력 되었습니다.")
    
# falsy: none, 0, 0.0, 빈컨테이너(빈 문자열, 빈 리스트, 빈 딕셔너리, 빈 튜플)
# pass, raise: 반복문, 조건문, 함수, 클래스에서 미구현 상태를 에러없이 지나감
data = "";
if data == 'data':
    # pass
    raise NotImplementedError;



""" 
2. 반복문
- while문 : 일정한 조건이 부합되면 계속 명령문 실행

- while문 문법
while 조건문:
    명령문
"""  
# value = 0;
# while value <= 10:
#     print("=")
#     value += 1
# else:
#     print("끝")
    
    
"""
- for문 : 일정한 조건 및 지정된 반복 수행할 횟수만큼 명령문 실행

- for문 문법
for 변수 in 시퀀스:
    명령문
"""

# 시퀀스: 문자열, 배열, 튜플, range
# text = 'python'
# for s in text:
#     print(s)

# range(start, end, step)
# for i in range(1,5,2):
#     print(i)

""" 반복문 실습
1) 20 이하 숫자중에서 4의 배수 출력하기
"""
# for i in range(1,21):
#     if(i % 4 == 0):
#         print(i, end = " ")
    


"""
2) 12를 찾아라
nums = [56, 73, 12, 5, 32, 24, 6, 10]

- 12를 찾으면 찾았다라는 문구 출력
- 응용 : 몇 번만에 찾았는지 한 눈에 알아보게 출력
"""
nums = [56, 73, 12, 5, 32, 24, 6, 10];
count = 1;


# for i in nums:
#     if i == 12:
#         print("{}번만에 찾았다".format(count));
        #   break;
#     else:
#         count += 1;

"""
3) 다중 for문으로 구구단 출력
- range 함수 이용
"""
for i in range(1,10):
    print("==============");
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j));
    