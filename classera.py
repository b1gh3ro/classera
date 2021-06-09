
#!/bin/bash

from selenium import webdriver
import asyncio
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from selenium.webdriver.common.keys import Keys
from dhooks import Webhook
from selenium.common.exceptions import NoSuchElementException
hook = Webhook('***REMOVED***')
PATH = "***REMOVED***"
driver = webdriver.Chrome(PATH)
driver.get('https://me.classera.com/student/vcrs')


async def main():
    username = driver.find_element_by_id('UserUsername')
    username.send_keys('***REMOVED***')
    password = driver.find_element_by_id('UserPassword')
    password.send_keys('***REMOVED***')
    password.send_keys(Keys.RETURN)
    close = driver.find_element_by_xpath('/html/body/div[17]/div/div/div[2]/button')
    close.click()
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    virtualclass = driver.find_element_by_id('box9')
    action = ActionChains(driver)
    action.move_to_element(virtualclass).perform()
    showall = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/div[12]/div/div/div[2]/div[2]/div[2]/a')

    showall.click()
    scroll = driver.find_element_by_tag_name('html') 
    scroll.send_keys(Keys.PAGE_DOWN)

    launch = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div[1]/div/div[2]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a')
    launchhov = ActionChains(driver)
    launchhov.move_to_element(launch).perform()
    try:
        launch = driver.find_element_by_xpath('/tml/body/div[6]/div/div[2]/div[5]/div[1]/div/div[2]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a')
        launchhov = ActionChains(driver)
        launchhov.move_to_element(launch).perform()
        launch.click()
        launched = ':white_check_mark: launched'
    except  NoSuchElementException:
        launched = ':negative_squared_cross_mark: launched'

    time.sleep(2)
    copy = driver.find_element_by_xpath('/html/body/div[19]/div/div[10]/button[1]').click()
    time.sleep(5)
    keyboard.send("tab", do_press=True, do_release=True)
    time.sleep(1)   
    keyboard.send("space", do_press=True, do_release=True) 
    time.sleep(10)
    hook.send(launched)
    driver.quit()

asyncio.run(main())