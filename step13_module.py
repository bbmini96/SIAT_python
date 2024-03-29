# Module
"""
module : 기능별로 코드 분리 (.py)
package : 기능이 비슷한 여러 모듈 모음(폴더)
library : 모듈, 패키지, 함수

import 모듈명 as 별칭
from 모듈 import 변수 as 별칭


모듈명.변수
모듈명.함수()
모듈명.클래스()

"""

import math as m # ModuleNotFoundError

# print(math.pi)
# print(math.sqrt(4))
# print(math.sqr(4)) # AttributeError

# print(m.pi)

from math import ceil as c, pi as p 

del m   # 삭제


# 랜덤
import random   # 0.0 <= random < 1.0
# print(random.random())

# random.randrange(start, end)   지정한 범위의 int값을 반환
# print(random.randrange(4,10))

# random.choice(리스트)
# print(random.choice([1,22,3,34,5,336,7]))

# random.sample(list, k=number)
# print(random.sample([3,4,5,1,2,33,34,51], k=2))

# 외부모듈 다운로드 pip install packageName  => cmd명령 프롬프트 창에서 

"""
numpy
과학 계산을 위한 라이브러리
행렬/배열 처리 및 연산
난수생성
"""
import numpy
# print(numpy.arange(10))

from urllib.request import urlopen

print(urlopen('https://naver.com'))






