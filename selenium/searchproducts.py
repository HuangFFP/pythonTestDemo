from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://172.16.5.12:4121/test02index")

# driver.find_element_by_class_name("login-us").send_keys("Selenium")
driver.find_element_by_class_name("login-us").send_keys("ctadmin")
driver.find_element_by_class_name("login-pw").send_keys("!2wsx")

#
# driver.find_element_by_id("su").click()
driver.find_element_by_class_name("login-btn").click()
print(driver.title)
dr = driver.find_element_by_css_selector("#navfour")
print(dr.get_attribute('title'))

# driver.quit()



