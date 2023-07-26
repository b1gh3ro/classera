
#!/bin/bash
from datetime import datetime
from re import T
from selenium import webdriver
import asyncio
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from selenium.webdriver.common.keys import Keys
from dhooks import Webhook
from selenium.common.exceptions import NoSuchElementException
hook = Webhook('<your-webhook>')
PATH = "<Path-to-chromedriver>"
driver = webdriver.Chrome(PATH)
driver.get('https://me.classera.com/student/vcrs')

hook.send("starting...")

def main():
    try:
        
        username = driver.find_element_by_id('UserUsername')
        username.send_keys(<usename>)
        password = driver.find_element_by_id('UserPassword')
        password.send_keys(<password>)
        password.send_keys(Keys.RETURN)
        
    except  NoSuchElementException:
        pass


    # html = driver.find_element_by_tag_name('html')
    # html.send_keys(Keys.PAGE_DOWN)
    # virtualclass = driver.find_element_by_id('box9')
    # action = ActionChains(driver)
    # action.move_to_element(virtualclass).perform()
    # showall = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/div[12]/div/div/div[2]/div[2]/div[2]/a')

    # showall.click()
    # scroll = driver.find_element_by_tag_name('html') 
    # scroll.send_keys(Keys.PAGE_DOWN)

    # launch = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/div/div[2]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a')
    # launchhov = ActionChains(driver)
    # launchhov.move_to_element(launch).perform()
    now = datetime.now()
    current_time = now.strftime('%Y/%m/%d %I:%M:%S')
    joined = False
    try:
    #     launch = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/div/div[2]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a')
    #     launchhov = ActionChains(driver)
    #     launchhov.move_to_element(launch).perform()
    #     launch.click()
        driver.get('https://me.classera.com/student')
        time.sleep(1)
       
        close = driver.find_element_by_xpath('/html/body/div[16]/div/div/div[3]/button[1]')
        close.click()
        className = driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/h4')
        join = driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div/a')
        join.click()
        launched = f'{className.text} just joined at {current_time} '
        joined = True
    except  NoSuchElementException:
        launched = f'{className.text} not joined time = {current_time} \n https://c.tenor.com/1FR4o42djy8AAAAM/spiderman-magic.gif'
        joined = False

    # time.sleep(2)
    try:
        copy = driver.find_element_by_xpath('/html/body/div[19]/div/div[10]/button[1]').click()
    except  NoSuchElementException:
        pass     
    if joined == True:
        time.sleep(5)
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(1)   
        keyboard.send("space", do_press=True, do_release=True) 
        time.sleep(10)
        hook.send(f'{launched}')
    else:
        hook.send(f'{launched}')
        pass
        


for i in range(50):    
    main()
    time.sleep(2400)
  
