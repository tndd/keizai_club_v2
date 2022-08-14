import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

load_dotenv()


def get_driver() -> webdriver.Edge:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.implicitly_wait(10)
    return driver


def login(driver: webdriver.Edge):
    driver.get('https://keizaiclub.com/member-login/')
    driver.find_element(By.CSS_SELECTOR, '#iump_login_username').send_keys(os.getenv('USERNAME_KC'))
    driver.find_element(By.CSS_SELECTOR, '#iump_login_password').send_keys(os.getenv('PASSWORD_KC'))
    driver.find_element(By.CSS_SELECTOR, '#ihc_login_form > div.impu-form-line-fr.impu-form-submit > input[type=submit]').click()


def main() -> None:
    d = get_driver()
    login(d)


if __name__ == '__main__':
    main()
