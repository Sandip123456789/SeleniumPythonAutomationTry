from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://www.thetestingworld.com/')

#scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

phone = driver.find_element(By.CLASS_NAME, "phone").text
print(phone)

email = driver.find_element(By.LINK_TEXT, "thetestingworld@gmail.com").text
print(email)

#scroll up
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

driver.find_element(By.LINK_TEXT, "Quick Demo").click()

driver.find_element(By.ID, "wdform_1_element_first2").send_keys("Allison")
driver.find_element(By.ID, "wdform_1_element_last2").send_keys("Becker")
driver.find_element(By.CSS_SELECTOR, "input#wdform_2_element2").send_keys("AB1@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input#wdform_4_element2").send_keys("07775218999")
driver.find_element(By.CSS_SELECTOR, "input#wdform_10_element2").send_keys("1999-07-07")

#for static dropdown use Select
select = Select(driver.find_element(By.CSS_SELECTOR, "select#wdform_5_element2"))
select.select_by_visible_text("DevOps")

driver.find_element(By.CSS_SELECTOR, "button.button-submit").click()

successMessage = driver.find_element(By.CSS_SELECTOR, "dd.message").text
assert "successfully submitted" in successMessage
print(successMessage)


