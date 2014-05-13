# -*- coding: utf-8 -*-
from __future__ import division

import time,re,sys
from selenium.webdriver.support.ui import Select



def loginStumble(driver, username, password):
    driver.implicitly_wait(120)
    driver.get("https://www.stumbleupon.com/login")
    driver.implicitly_wait(180)
    driver.find_element_by_id('user').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id("login").click()
    global all_cookies
    all_cookies = driver.get_cookies()
    html = driver.page_source
    print username + ' is logged in'
    return html

def likePage(driver,url):
    driver.implicitly_wait(3)
    print 'like url : ' + url
    url = 'http://www.stumbleupon.com/submit?url='+url
    driver.get(url)
    driver.find_element_by_id("safe").click()
    driver.implicitly_wait(60)
    select = Select(driver.find_element_by_name('tags'))
    driver.find_element_by_xpath("//a[@class='chzn-single']").click()
    driver.find_element_by_xpath("//li[@id='tags_chzn_o_44']").click()
    driver.find_element_by_id("user-tags").send_keys('Babes, boobs, girl, boobies, sexy, sexiest')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
    return driver.page_source