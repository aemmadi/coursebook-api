# Import Libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Scrape coursebook, given the formatted course tag (Ex: cs4337.001.20f)


def webscrape(course_tag):

    # Configure chromedriver
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome("bin/chromedriver", chrome_options=opt)

    # Scrape coursebook
    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    elem = driver.find_element_by_link_text("Class Detail")
    time.sleep(0.1)  # Prevents coursebook to freeze due to fast executions
    elem.click()
    driver.implicitly_wait(1.5)  # Wait for new data to render on coursebook
    elem = driver.find_elements_by_class_name("courseinfo__overviewtable__td")

    # Data processing
    classData = []
    for obj in elem:
        classData.append(obj.text)  # Dumps all data into a list

    # Finishing touches
    driver.quit()
    return classData
