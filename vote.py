

import time
import os
while True:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    chromedriver = ""#write here the location of chromdriver on your machine
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://thegreatpageantcommunity.com/2017/09/07/miss-diva-2017-contestants-vote-for-your-favourite/")#write here the address of your webpage
    elem = driver.find_element_by_id('PDI_answer44965573').click()
    elem = driver.find_element_by_id('pd-vote-button9825261').click()
    time.sleep(1)
    driver.close()



#Author: Aman Hirani
#date: 10 September,2017
#time:4:20:42 hours
