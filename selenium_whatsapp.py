from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driverPath = "driver/chromedriver.exe"
driver = webdriver.Chrome('/path/to/chromedriver')     #executable_path = driverPath
driver.get('https://web.whatsapp.com')

name = input('name: ')
msg = input('messagge:')
count = int(input('count: '))

user = driver.find_element_by_xpath('//span[tittle = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_2sivp')



# wassup_url = r'https://web.whatsapp.com/send?phone={ur_mobile_number}&text&app_absent=0'

# driver = webdriver.Chrome(r'C:\Users\jay\Desktop\PythonInOffice\amazon_price_alert_bot\chromedriver.exe')

# driver.get(wassup_url)
