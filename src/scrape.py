import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def webscrape(course_tag):
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome("bin/chromedriver.exe", chrome_options=opt)

    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    elem = driver.find_element_by_link_text("Class Detail")
    time.sleep(1)
    elem.click()
    driver.implicitly_wait(3)
    elem = driver.find_elements_by_class_name("courseinfo__overviewtable__td")

    classData = []
    for obj in elem:
        classData.append(obj.text)

    driver.quit()
    return classData
