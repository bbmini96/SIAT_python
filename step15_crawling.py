# Crawling

# step01) requests
"""
response = requests.request(url)
response.content:   # html 문서(byte)
response.text:      # html 문서(문자열)
response.status_code:   # status_code 확인
response.headers:   # 헤더 확인

"""

import requests
from bs4 import BeautifulSoup

response = requests.request('GET','https://en.wikipedia.org/wiki/Python')
# print(response.text)


# step02) BeautifilSoup
"""
from bs4 import BeautifulSoup
BeautifilSoup(대상객체, 파싱의 형식) 
BeautifulSoup(response.content,'html.parser'),
BeautifulSoup(response.content,'html5lib'),
BeautifulSoup(response.content,'csv'),
BeautifulSoup(response.content,'xml')
BeautifulSoup(response.content,'lxml')

.find('태그명')
.find_all('태그명')  

soup.find_all(id="footer-copyrightico") # id값으로 가져오기
soup.find_all(class_="mw-headline")     # class 값으로 가져오기
soup.select('') # css 문법으로 해당 객체를 검색

bs4.element.Tag.get_text() # Tag 내부의 content 출력

"""
# soup = BeautifulSoup(response.content,'html.parser')
# print(soup.find_all('li'))


# find_all(id)
# li_tags = soup.find_all(id="footer-copyrightico")
# for li_tag in li_tags:
#     print('---', li_tag)
#     print('')    

# find_all(class)
# h2_tags = soup.find_all(class_="mw-headline")
# for h2_tag in h2_tags:
#     print(h2_tag)

# #select(css문법으로)
# h2_tags = soup.select(".mw-headline")
# for h2_tag in h2_tags:
#      print(h2_tag)


# get_text() #태그 내부의 content출력
# h2_tags = soup.select(".mw-headline")
# for h2_tag in h2_tags:
#      print(h2_tag.get_text())



# 실습)
response_forves = requests.request('GET','https://www.forbes.com/advisor/credit-cards/travel-rewards/best-places-to-travel/')

soup_forves = BeautifulSoup(response_forves.content,'html.parser')
# trv_names = soup_forves.find_all('h3')
trv_names = soup_forves.find_all('h3', id =True)

count = 0

with open('forves.txt', 'w', encoding='UTF-8') as f:
    for trv_name in trv_names:
        count += 1
        result = f"{count} {trv_name.get_text()}"
        print(result)
        f.write(str(result))
        f.write('\n')





