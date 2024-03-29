#selenium
"""
- js로 동적으로 생성되는 정보를 크롤링 하기 위한 라이브러리
- HTML요소를 컨트롤(버튼 클릭, 입력,.... 이벤트) 가능

- 세팅
    - pip install selenium
    - 브라우저(크롬: 버전확인!) 드라이버 설치
    
- 사용
    - from selenium import webdriver
    - webdriver.Chrome("C:\driver") # 드라이버의 위치
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()

# get(url)
driver.get(url="https://naver.com")

time.sleep(5)