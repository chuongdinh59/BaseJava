from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service('/venv/chromedriver.exe'))
    driver.get('https://lms.ou.edu.vn/')
    driver.fullscreen_window()
    btn1 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.main-btn')))
    # btn1 = driver.find_element(By.CSS_SELECTOR, '.main-btn')
    btn1.click()

    btn2 = driver.find_element(By.CSS_SELECTOR, '.login100-form-btn')
    btn2.click()

    form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login_form')))
    username = driver.find_element(By.ID,'form-username')
    password = driver.find_element(By.ID,'form-password')
    username.send_keys("2051052012")
    password.send_keys("079202019041")
    type = Select(driver.find_element(By.ID, 'form-usertype'))
    type.select_by_index(1)
    type.select_by_index(2)
    type.select_by_index(3)
    input()
    btn3 = driver.find_element(By.CSS_SELECTOR, ".m-loginbox-submit-btn")
    btn3.click();

    card_desk = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#page-container-2 div.card-deck')))

    courses = card_desk.find_elements(By.CSS_SELECTOR, ".card.dashboard-card")
    # course = driver.find_elements(By.CSS_SELECTOR, ".card-desk .card.dashboard-card")
    print(courses)

    for course in courses:
        span = course.find_element(By.CSS_SELECTOR, ".multiline")
        if span:
            print(span.text)
    driver.quit()





    #  driver.switch_to.window(driver.window_handles[-1])
    #  driver.fullscreen_window()
    #  type = Select(driver.find_element(By.ID, 'form-usertype'))
    #  type.select_by_index(1)
    #  type.select_by_index(2)
    #  type.select_by_index(3)
    #  driver.execute_script("window.scrollTo(0,200)")
    #  driver.save_screenshot("D:/abc.jpg")
    #  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#excel-table > tbody > tr.text-center.ng-star-inserted")))
    #  scores = driver.find_elements(By.CSS_SELECTOR, "#excel-table > tbody > tr.text-center.ng-star-inserted")
