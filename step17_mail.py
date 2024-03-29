# sending email with python
"""
- SMTP(Simple Mail Transfer Protocol) : 메일 서버 전송 규약
- POP(Post Office Protoco)3 : 사용자의 기기로 이메일을 다운로드(서버에 메일 저장X)
- IMAP(nternet Message Access protocol) :  사용자의 기기에서 이메일에 액세스 가능(서버에 메일 저장O)
- MIME(Multipurpose Internet Mail Extensions) : 이메일 전송시 인터넷 표준 포맷
    - https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    - MIMEMultipart : 메일의 본문 내용을 만드는 모듈
        from email.mime.multipart import MIMEMultipart
    - MIMEText, MIMEApplictation : 메일 본문에 담길 내용, 파일
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
    
- smtplib
    - 파이썬에서 STMP를 활용하여 메일 전송 기능을 제공하는 표준 라이브러리
    import smtplib

- 메일 전송 필요 데이터
    - SMTP_SERVER = 'smtp.gmail.com'
    - SMTP_PORT = 465
    - SMTP_USER
    - SMTP_PASSWORD
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# 환경 변수
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = '이메일'
SMTP_PASSWORD = '비번'

# 기본 내용 및 구조
msg = MIMEMultipart('mixed') # 텍스트 + 파일

msg['From'] = SMTP_USER
msg['To'] = SMTP_USER
msg['Subject'] = '메일 전송 테스트'


# 내용
msg_text = '내용'
text = MIMEText(msg_text,'html', _charset = 'UTF-8')
msg.attach(text)

# file 전달
file_name = 'test.txt'
with open(file_name,'rb') as f:
    transfer_file = MIMEApplication(f.read())
    transfer_file.add_header('Content-Disposition','attachment', filename ='mail.txt')
    msg.attach(transfer_file)
    
# 메일 전송
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(SMTP_USER, SMTP_PASSWORD)
smtp.sendmail(SMTP_USER, SMTP_USER, msg.as_string())
smtp.close()
