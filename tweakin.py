#coding=utf-8
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji


while True:

 driver = webdriver.Chrome('/Users/admin/Downloads/chromedriverreal')
 driver.get('https://www.instagram.com/')
 driver.maximize_window()
 time.sleep(1)

 username = driver.find_element_by_name("username")
 username.send_keys("donut_rising") #donut_rising
 time.sleep(1)

 password  = driver.find_element_by_name("password")
 password.send_keys("donut12!") #donut12!


 time.sleep(1)

 def clickentry():
  login =  driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
  login.click()
  return;

 clickentry();

 time.sleep(4)

 driver.get('https://www.instagram.com/')

 def notif():
  notnow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
  notnow.click()
  return;

 notif();

 time.sleep(2)

 donut = ('ah he tweakin 🍩')   
 comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[3]/div/article[1]/div[3]/section[3]/div/form/textarea')
 time.sleep(1)
 comment.click()
 comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[3]/div/article[1]/div[3]/section[3]/div/form/textarea')
 comment.click()


 driver.execute_script("arguments[0].innerHTML = '{}'".format(donut),comment)

 comment.send_keys('n')

 time.sleep(2)

 post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article[1]/div[3]/section[3]/div/form/button[2]')
 post.click()


 time.sleep(10)

 driver.close()

 if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
