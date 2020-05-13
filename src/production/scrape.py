# Import Libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

# Scrape coursebook, given the formatted course tag (Ex: cs4337.001.20f)


def webscrape(course_tag):

    # Configure chromedriver
    opt = Options()
    opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=opt)

    # Scrape coursebook
    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    elem = driver.find_element_by_link_text("Class Detail")
    time.sleep(0.5)  # Prevents coursebook to freeze due to fast executions
    elem.click()
    driver.implicitly_wait(3)  # Wait for new data to render on coursebook
    elem = driver.find_elements_by_class_name("courseinfo__overviewtable__td")
    elem_head = driver.find_elements_by_class_name(
        "courseinfo__overviewtable__th")

    # Data processing
    classData = []
    classHead = []

    # Dumps all data into a list
    for obj in elem:
        classData.append(obj.text)

    for obj in elem_head:
        classHead.append(obj.text)

    # Finishing touches
    driver.quit()
    return {
        'data': classData,
        'head': classHead
    }
