import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mvnrepository.com/")
#  //*[@id="left"]/div[2]/ul/li[1]/a
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/ul/li[1]/a").click()


time.sleep(5)

driver.close()

