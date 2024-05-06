from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

def get(url):

    driver = webdriver.Chrome()
    driver.get("https://instafinsta.net/")


    url_t_box = driver.find_element(By.XPATH, '//*[@id="url"]')
    url_t_box.send_keys(url)

    sleep(2)

    find_btn = driver.find_element(By.XPATH, '//*[@id="form_submit"]')
    find_btn.click()

    sleep(6)

    download_btn = driver.find_element(By.XPATH, '//*[@id="downloadbox"]/div/div/div/div/a')
    download_btn.click()


    while(True):
        input("Enter any key to quit! ")
        break

    driver.quit()


if __name__ == "__main__":
    url = sys.argv[1]
    get(url)
