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
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# get(url)
# driver.get(url="https://naver.com")

# time.sleep(2)

# step01 치지직 사이트 접속
# 자동화: 치지직 태그 객체로 반환 -> 클릭
"""
driver.find_element(By.항목,값)
from selenium.webdriver.common.by import by
By.항목: ID,CSS_SELECTOR,....
"""
# a_tag = driver.find_element(By.CSS_SELECTOR, '#shortcutArea > ul > li:nth-child(10) > a')
# ActionChains 클릭
# ActionChains(driver).click(a_tag).perform()
# time.sleep(5)





#===============================================

# step02 naver 메인 페이지 -> '점심메뉴' 입력 -> 검색
# send_keys: 입력
# search_input = driver.find_element(By.ID,'query').send_keys('점심메뉴')
# search_btn = driver.find_element(By.CSS_SELECTOR, '#sform > fieldset > button')
# ActionChains(driver).click(search_btn).perform()
# time.sleep(5)

# print(driver.page_source)       # 페이지 소스 가져오기




#=======================================================================
# 인터파크 투어에서 터미널에서 내가 입력한 도시 이름으로 해외 패키지 내용 출력하기
from bs4 import BeautifulSoup
driver.get(url="https://mtravel.interpark.com/home")
driver.set_window_size(1100, 3000)

search_input= input()
driver.find_element(By.ID, 'divHeaderSearch').click()
search_input = driver.find_element(By.ID,'txtHeaderInput').send_keys(search_input)
search_btn = driver.find_element(By.ID, 'btnHeaderInput')
ActionChains(driver).click(search_btn).perform()
more_btn = driver.find_element(By.CSS_SELECTOR,'div.searchAllBox.overseaTravel.col1 > div > button')
ActionChains(driver).click(more_btn).perform()

select_title = driver.find_element(By.CSS_SELECTOR, "h5.infoTitle")

time.sleep(5)














































