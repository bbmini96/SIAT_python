# file I/O

# open('파일명','모드)

# V1
# f = open('test.txt','w',encoding='UTF-8')
# f.write('파이썬')
# f.write('Python')
# f.close()

# V2 with open()
contents = ['파이썬\n', 'python']
with open('output1.txt', 'a', encoding='UTF-8') as f:
    # f.writelines('잠온다\n')
    # f.writelines('I want sleep')
    f.writelines(contents)
    
# read
# 존재 하지 않는 파일 에러 발생
# with open('output1.txt', 'r', encoding='UTF-8') as f:
#     x, y, z = f
#     print(x)
#     print(y)
    # print(f.read())   # 파일에 있는 전체를 문자 열로 가져온다
    # lines = f.readline() # 한줄만 출력해주는 함수
    # print(lines)
    # for line in lines:
    #     print(line.strip('\n'))
    # line = None
    # while line != '':
    #     line = f.readline()
    #     print(line.strip('\n'))
    

# p1 numpy.txt #으로 시작하는 주석 문장만 출력
# with open('numpy.txt', 'r', encoding='UTF-8') as numpyT:
#   with open('numpy.txt', 'w', encoding='UTF-8') as fo:
#     lines = numpyT.readlines()
#     for lineT in lines:
#         if lineT.startswith("#"):
#             fo.writelines(lineT)
    # numpyT.close()

# p2 numpy_line.txt 생성(조건: numpy.txt 내용 그대로 가져오되 각 라인 앞에 라인 넘버 붙여서 표현)

# idx = 0
# with open('numpy.txt', 'r', encoding='UTF-8') as fi:
#     with open('numpy_line.txt', 'w', encoding='UTF-8') as fo:
#         for line in fi.readlines():
#             idx += 1
#             fo.writelines(f'{idx}: {line}')

# 추가) numpy.txt -> 단어 빈도수: 체크 기능
# 정의) 띄어쓰기를 기준, dict {단어: 빈도수}
# Counter 기능: from collections import Counter
# 사용) counter([numpy.txt -> split()])

from collections import Counter
lines = open('numpy.txt', 'r', encoding= 'UTF-8')

word_dict = dict(Counter(lines.read().split()))

search_keyword = input("단어를 입력해 주세요")

print(f'검색한 단어는 {search_keyword}이고, 횟수는{word_dict[search_keyword]}입니다')

lines.close()










  
    
    
