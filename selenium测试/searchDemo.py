#1.导包
from selenium import webdriver
#2.创建浏览器对象
driver = webdriver.Chrome()
#3.打开浏览器首页
driver.get('https://www.google.ca/')
#4.在搜索框中输入selenium
driver.find_element_by_name('q').send_keys('selenium')
#5.点击搜索按钮
driver.find_element_by_name('btnK').click()
#6.关闭浏览器
driver.quit()

