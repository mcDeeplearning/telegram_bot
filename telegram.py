import requests
from bs4 import BeautifulSoup
token = "763337042:AAEjq0JPofKKdu9_oYwVdi5O5L8JGz_xl6E"
method_name = "getUpdates"
url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
update = requests.get(url).json()

user_id = update["result"][0]['message']['from']['id']
method_name = "sendmessage"

url_cos = "https://finance.naver.com/sise/"
html_cos = requests.get(url_cos).text
soup_cos = BeautifulSoup(html_cos, 'html.parser')
select = soup_cos.select_one('#KOSPI_now')

msg = select.text
msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
# print(msg_url)
print(requests.get(msg_url))




