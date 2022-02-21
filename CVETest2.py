import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
s = Service('C:\ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)


def grab(targeturl):
    driver.get(targeturl)


try:
    for i in range(1):
        webPage = input("What is your CVE from Microsoft? (copy and paste the url)\n")
    grab(webPage)
except:
    print("Invalid URL")
    driver.quit()
    sys.exit()


print(WebDriverWait(driver, 8).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'CVE')]"))).text)
print("Impacted: " + WebDriverWait(driver, 8).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text)
print("CVSS Detail is: " + WebDriverWait(driver, 8).until(EC.visibility_of_element_located(
    (By.XPATH, "//label[starts-with(@class, 'ms-Label') and starts-with(., 'CVSS')]"))).text)
# . is same as text()
print("Attack Vector: " + WebDriverWait(driver, 8).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@role='gridcell' and .//summary[contains(.,'Attack Vector')]]/following::div[1]//summary"))).text)
print("Exploited?: " + WebDriverWait(driver, 8).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-automation-key='exploited']"))).text)
Download = WebDriverWait(driver, 8).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "i[data-icon-name='Download']")))
Download.click()
StartDownload = WebDriverWait(driver, 8).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Start')]")))
StartDownload.click()
print("Attached is the 'XLSX' and available security update regarding the vulnerability.")
# driver.quit()
