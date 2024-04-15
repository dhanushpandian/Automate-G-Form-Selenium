from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

web=webdriver.Chrome()

form="https://docs.google.com/forms/d/e/1FAIpQLSfcKPE0HNEWdM3gpn1O94AoBUz5oKBUBVwPooywKe80UeeRCg/viewform?usp=sf_link"

web.get(form)
time.sleep(2)

sname="sara"
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)

dob="12/12/1999"
phone=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
phone.send_keys(dob)

opt1_button=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')
opt1_button.click()

select_dropdown=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
select_dropdown.click()
time.sleep(2)
opt2_button=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span')
opt2_button.click()
# dropdown = Select(select_dropdown)
# dropdown.select_by_visible_text('Option Text')  
# select_dropdown.select_by_index(2)
# option_value = 'Option 2'
# web.execute_script("arguments[0].value = '{}';".format(option_value), select_dropdown)

# parent_element = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
# select_dropdown = web.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[4]/span')
# option_value = 'Option 2'
# web.execute_script("arguments[0].value = '{}';".format(option_value), select_dropdown)


time.sleep(20)
submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()