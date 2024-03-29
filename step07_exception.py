"""
Exception

try:
    수행코드
except 예외 타입:
    예외가 발생 했을때 처리하는 수행 코드
else:
    예외가 발생하지 않았을때 처리하는 수행 코드
finally:
    예외 여부 발생 상관 없이 항상 실행하는 수행 코드
    
"""

# def divide(x):
#     result = 0
#     try:
#         result = 10 / x
#         return result
#     except ZeroDivisionError as e:
#         return e
#         # return '0으로는 나눌 수 없음'
#     except TypeError:
#         return "문자열로 숫자를 나눌 수 없음"
#     except Exception:
#         return '정의 하지 않은 예외 처리'
        
# print(divide("10"))
# print(divide(10))
# print(divide(0))

# else, finally
# def change_number_type():
#     # x -> 숫자(int)로 변경
#     #   -> 예외 발생
#     try:
#         input_number = int(input('숫자를 입력하시오.'))
#         print(input_number)
#     except:
#         print('입력한 값을 확인하세요.')
#     else:
#         print('예외가 발생하지 않았을 때 수행 코드.')
#     finally:
#         print('반드시 실행되는 코드')
    
# change_number_type()


# finally 실전
# def open_file(file_name):
#     try:
#         f = open(file_name,'r',encoding='UTF-8')
        
#     except:
#         print('존재하지 않는 파일 입니다')
#     else:
#         print(f.read())
#     finally:
#          f.close()

# open_file('pandas.txt')



# def divide(x):
#     result = 0
#     try:
#         result = 10 / x
#     except ZeroDivisionError:
#         return '0으로는 나눌 수 없음'
#     except TypeError:
#         return "문자열로 숫자를 나눌 수 없음"
#     except Exception:
#         return '정의 하지 않은 예외 처리'
#     else:
#         print('예외가 발생하지 않았을 때 수행 코드.')
#     finally:
#         print('반드시 실행되는 코드')
        
# print(divide("10"))
# print(divide(10))
# print(divide(0))


# raise Exception("예외 메세지")
def multiple_seven():
    x = int(input('7의 배수 입력 : '))
    if (x % 7) != 0:
        raise Exception("7의 배수가 아님")
    print(x)

try:
    multiple_seven()
except Exception as e:
    print(f'예외 발생 : {e}')