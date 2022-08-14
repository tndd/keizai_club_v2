import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

load_dotenv()


def get_driver():
    return webdriver.Edge(EdgeChromiumDriverManager().install())


def login(driver: webdriver.Edge):
    driver.get('https://keizaiclub.com/member-login/')
    driver.find_element(By.CSS_SELECTOR, '#iump_login_username').send_keys(os.getenv('USERNAME_KC'))
    driver.find_element(By.CSS_SELECTOR, '#iump_login_password').send_keys(os.getenv('PASSWORD_KC'))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#ihc_login_form > div.impu-form-line-fr.impu-form-submit > input[type=submit]').click()


def login_ggl(driver: webdriver.Edge):
    driver.get('https://www.google.co.jp/')
    driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').send_keys('gabe the dog')
    driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b').click()


def main() -> None:
    d = get_driver()
    login_ggl(d)


if __name__ == '__main__':
    main()
