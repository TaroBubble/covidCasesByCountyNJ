from bs4 import BeautifulSoup
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
# -*- coding: utf-8 -*-

dataList = []
countyList = []
newPositives = []
confirmedDeaths = []
totalPosTests = []
probableDeaths = []
url = "https://maps.arcgis.com/apps/opsdashboard/index.html#/ec4bffd48f7e495182226eee7962b422"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)
htmlSource = driver.page_source
driver.quit()
page = BeautifulSoup(htmlSource, 'html.parser')
doc = page.find_all('span',{'class':'flex-horizontal feature-list-item ember-view'})

for county in doc:
    countyNames = county.find('strong')
    countyList.append(countyNames.getText())

countyList.pop(0)
countyList.pop(0)
countyList.pop(len(countyList)-1)
countyList.pop(len(countyList)-1)

for data in doc:
    datas = data.select('td')
    for strong in datas:
        strongTags = strong.select('strong')
        for span in strongTags:
            rawData = span.select('span')
            for data in rawData:
                dataList.append(data.getText())

print(dataList)

for i in dataList[::4]:
    newPositives.append(i)

for i in dataList[1::4]:
    confirmedDeaths.append(i)

for i in dataList[2::4]:
    totalPosTests.append(i)

for i in dataList[3::4]:
    probableDeaths.append(i)

print(newPositives)
print(confirmedDeaths)
print(totalPosTests)
print(probableDeaths)

countyData = list(zip(countyList, newPositives, confirmedDeaths, totalPosTests, probableDeaths))
print(countyData)