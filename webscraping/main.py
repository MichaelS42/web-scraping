from bs4 import BeautifulSoup
import requests


html_text = requests.get('')

soup = BeautifulSoup(html_text, 'lxml')
data = soup.find('li', class_ = 'js inspect elements')
data_name = job.find('element', class_ = 'classname')