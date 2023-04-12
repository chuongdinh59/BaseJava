from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service('/venv/chromedriver.exe'))
    driver.get('https://tienichsv.ou.edu.vn/#/home')

    driver.implicitly_wait(1000)
    btn1 = driver.find_element(By.CSS_SELECTOR, 'button.ng-star-inserted.btn-success')

    btn1.click()

    driver.switch_to.window(driver.window_handles[-1])
    form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login_form')))
    username = driver.find_element(By.ID,'form-username')
    password = driver.find_element(By.ID,'form-password')

    username.send_keys("2051052012")
    password.send_keys("079202019041")

    btn3 = driver.find_element(By.CSS_SELECTOR, ".m-loginbox-submit-btn")
    btn3.click();
    driver.implicitly_wait(5000)
    a_diem = driver.find_element(By.CSS_SELECTOR, "div > ul:nth-child(8) > li > div.text-cus > a:nth-child(1)")
    print(a_diem.get_attribute("title"))
    driver.fullscreen_window()
    a_diem.click()
    driver.implicitly_wait(5000)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#excel-table > tbody > tr.text-center.ng-star-inserted")))
    scores = driver.find_elements(By.CSS_SELECTOR, "#excel-table > tbody > tr.text-center.ng-star-inserted")

    driver.execute_script("window.scrollTo(0,200)")
    driver.save_screenshot("D:/abc.jpg")
    for score in scores:
        name = score.find_element(By.CSS_SELECTOR, 'td.align-middle.text-left')
        score1 = score.find_element(By.CSS_SELECTOR, 'td:nth-child(7)')
        score2 = score.find_element(By.CSS_SELECTOR, 'td:nth-child(8)')
        score3 = score.find_element(By.CSS_SELECTOR, 'td:nth-child(10)')
        score4 = score.find_element(By.CSS_SELECTOR, 'td:nth-child(11)')
        print(name.text + "-" + score1.text + "-" + score2.text + "-" + score3.text + "-"  + score4.text)
    driver.quit()


