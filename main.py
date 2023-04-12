from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(service=Service('/venv/chromedriver.exe'))
# driver.get('https://lms.ou.edu.vn/')
#
# btn1 = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="about"]/div[1]/div/div[1]/div/a[1]')))
# btn1.click()
# btn2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="region-main"]/div/div/div/div/div/div/form/div[3]/button')))
# btn2.click()
#
# username = driver.find_element(By.XPATH, '//*[@id="form-username"]')
# password = driver.find_element(By.XPATH, '//*[@id="form-password"]')
# password.send_keys("079202019041")
# username.send_keys("2051052012")
#
# btn3 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="login_form"]/div[4]/div/button')))
# btn3.click()
#
#
#
# courses = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div')))
#
#
# for course in courses:
#     card = driver.find_element(By.CSS_SELECTOR, '.card.dashboard-card')
#     span = card.find_element(By.CSS_SELECTOR, 'a span.multiline')
#     print(span.text)
# driver.quit()
