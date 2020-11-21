from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\CHANDAN SAHU\Desktop\chromedriver")
driver.get('https://collegedunia.com/bangalore-colleges')
driver.maximize_window()
time.sleep(30)
print(1)
driver.find_element_by_xpath('//*[@id="js-lead-btn-close"]').click()
time.sleep(30)
print(2)

# page loading for total data 
last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = 10
print(3)
count = 0
while True:
    count+=1
    driver.execute_script('window.scrollTo(0,'+str(last_height//2+last_height//3)+')')
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(count)
    if new_height == last_height:
        break
    last_height = new_height
    time.sleep(1.2)

html = driver.execute_script('return document.documentElement.outerHTML')
f=open("pune.html","w+",encoding = 'UTF-8')
f.write(html)
print("done")
