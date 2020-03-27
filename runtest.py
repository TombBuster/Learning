from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import urlopen
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.gsa-spark.com/speedtest/0a1e06b5-e92f-48ee-a6bd-0b83f907beda")

#STRIPPING FROM WEBSITE

#obtaining data from website
quote_page = 'https://www.gsa-spark.com/speedtest/0a1e06b5-e92f-48ee-a6bd-0b83f907beda'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

#Get the first number
numb1 = soup.find('span', {'id': 'number1'})
num1 = numb1.text.strip()
n1 = int(num1)

#Get the second number
numb2 = soup.find('span', {'id': 'number2'})
num2 = numb2.text.strip()
n2 = int(num2)

#find the sum:
s = n1 + n2
s = str(s)





#INPUT INTO TEXT BAR






inputElement = driver.find_element_by_id("answer")
inputElement.send_keys(s)
inputElement.send_keys(Keys.ENTER)
