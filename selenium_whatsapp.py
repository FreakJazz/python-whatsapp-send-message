from selenium import webdriver

wassup_url = r'https://web.whatsapp.com/send?phone={ur_mobile_number}&text&app_absent=0'

driver = webdriver.Chrome(r'C:\Users\jay\Desktop\PythonInOffice\amazon_price_alert_bot\chromedriver.exe')

driver.get(wassup_url)
