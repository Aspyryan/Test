import base64
import imaplib

from bs4 import BeautifulSoup

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "piemelwaterJr" + ORG_EMAIL
FROM_PWD = "I3u2mB5xfqyy"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def readmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)

    mail.select('inbox')

    typ, data = mail.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mail.fetch(b'5', '(RFC822)')

        print(data[0][1].decode("utf-8"))


readmail()