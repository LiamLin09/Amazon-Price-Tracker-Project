import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())

price = soup.find(class_='a-offscreen').get_text()
print(price)
price_without_currency = price.split('$')[1]
print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id='productTitle').getText().strip()
print(title)
YOUR_EMAIL = ''
YOUR_PASSWORD = ''

BUY_PRICE = 200
if price_as_float < BUY_PRICE:
    message = f'{title} is now {price}'

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f'Subject: Amazon Price Alert\n\n{message}\n{url}'.encode('utf-8')
        )


