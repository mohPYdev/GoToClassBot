from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def login(driver , user , passw):
    username = driver.find_element(By.ID , 'username')
    username.clear()
    username.send_keys(user)

    password = driver.find_element(By.ID , 'password')
    password.clear()
    password.send_keys(passw)

    #submit 
    driver.find_element(By.ID , 'submit').click()
    print('successfully logged in')


def main():
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get("http://lms.ui.ac.ir")
    driver.find_element(By.ID , 'annonmentc').click()
    login(driver , '983613022' , '1273378679')
    driver.get('http://lms.ui.ac.ir/members/home')
    time.sleep(60)
    classXpath = '//*[@id="meetings_upcoming"]/li[1]/table/tbody/tr/td[2]/a'
    listenOnlyXpath = '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]'
    driver.find_element(By.XPATH, classXpath).click() #go tho class
    driver.find_element(By.XPATH, listenOnlyXpath).click()  #click on listen only
    time.sleep(3600) #wait an hour in the class
    driver.quit()


if __name__ == '__main__':
    main()



