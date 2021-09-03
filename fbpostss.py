#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium.webdriver.common.keys import Keys
import random   
from datetime import datetime 
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from io import StringIO
import csv
from selenium import webdriver
import time
import pandas as pd


# In[3]:


driver2 = webdriver.Chrome("chromedriver.exe")
driver2.get('https://www.facebook.com/')
time.sleep(2)
driver2.find_element_by_name('email').send_keys('perfectnikhil1697@gmail.com')
time.sleep(2)
# print("sadasdas")
driver2.find_element_by_name('pass').send_keys('C@lesthenics1698')
time.sleep(5)
driver2.find_element_by_name('login').click()


# In[36]:


driver3 = webdriver.Chrome("chromedriver.exe")
driver3.get('https://www.facebook.com/')
time.sleep(2)
driver3.find_element_by_name('email').send_keys('perfectnikhil1697@gmail.com')
time.sleep(2)
# print("sadasdas")
driver3.find_element_by_name('pass').send_keys('C@lesthenics1698')
time.sleep(5)
driver3.find_element_by_name('login').click()


# In[52]:


with open('posts.csv','w',newline='',encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["post_url","username","post_img","post_text","likes","comment","shares"])


# In[53]:


driver2.get('https://www.facebook.com/moshik.kovarsky')
time.sleep(6)

driver2.execute_script("window.scrollTo(0, 500);")
#time.sleep(1)

time.sleep(2)


posts=[]
for i in range(0,15):
    driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
post_urls=[]
    
while True:
    post_img="null"
    post_text="null"
    likes="null"
    comment="null"
    share="null"
    post_url="null"
    last_height = driver2.execute_script("return document.body.scrollHeight")
    post=driver2.find_elements_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l tm8avpzi']")
    for i in post:
        post_uri=i.get_attribute('href')
        # print(post_image)
        if post_uri not in post_urls:
            post_urls.append(post_uri)
            post_img="null"
            post_text="null"
            likes="null"
            comment="null"
            share="null"
            post_url="null"
            username="null"
            driver3.get(post_uri)
            time.sleep(5)
            try:
                post_img=driver3.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']/img").get_attribute('src')
            except:
                pass
            try:
                post_text=driver3.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']").text
            except:
                pass
            try:
                likes=driver3.find_element_by_xpath("//span[@class='pcp91wgn']").text
            except:
                pass

            try:
                comments=driver3.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain']")
            except:
                pass

            try:
                comment=comments[0].text
            except:
                pass

            try:
                share=comments[1].text
            except:
                pass
            try:
                username=driver3.find_element_by_xpath("//h2[@class='gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu']").text
            except:
                pass

            
            with open('posts.csv','a',newline='',encoding='utf-8') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([post_uri,username,post_img, post_text, likes ,comment, share])
            
    #                 print(l)
    time.sleep(2)
    driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)
    new_height = driver2.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height









