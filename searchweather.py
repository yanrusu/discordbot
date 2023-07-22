from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.safari.options import Options


driver = webdriver.Safari()
# 載入網頁
driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000203")
# 取得網頁內容
web = driver.page_source
driver.quit()
# 解析網頁
soup = BeautifulSoup(web, 'html.parser')

# web = requests.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000203")
# print(web.text)
# soup = BeautifulSoup(web.text, 'html.parser')

table = soup.find('div', accesskey="K")
table1 = table.find('div',id="PC_week")
table2 = table1.find('div',class_="table-responsive report-table pc grid_open")
table3 = table2.find('table',id="TableId3hr")
table4 = table3.findAll('td',headers = "PC3_Po")

#全部三小時天氣降雨
w = []

for i in range(len(table4)):
    hrwt = table4[i].get_text()
    if i == 1 or i == 2:
        print(i)
        if hrwt != '0%':
            #加入list
            w.append(int(hrwt[:2]))
        else:
            w.append(0)

rain4 = False ; rain6 = False ; rain7 = False ; norain = False

for i in range(len(w)):
    if w[i]>=70:
        rain7 =True
    elif w[i]>=60:
        rain6 = True
    elif w[i]>=40:
        rain4 = True
    else: 
        norain = True
status=''

if rain7:
    status = '降雨率 70% 以上，記得帶拖鞋'
if rain6:
    status = '降雨率 60% 以上，'
if rain4:
    status = ''
if norain:
    status = ''

print(status)