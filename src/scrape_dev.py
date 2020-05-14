# Import Libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import production.functions.data as data
import sys

# Configure chromedriver
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--no-sandbox")


def spawn_browser():
    spawn = webdriver.Chrome("bin/chromedriver-win.exe", chrome_options=opt)
    return spawn


# Scrape coursebook, given the formatted course tag (Ex: cs4337.001.20f)


def webscrape(course_tag):
    driver = spawn_browser()
    # Scrape coursebook for one specific course
    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    course = driver.find_element_by_link_text("Class Detail")
    time.sleep(0.5)  # Prevents coursebook to freeze due to fast executions
    course.click()
    driver.implicitly_wait(3)  # Wait for new data to render on coursebook
    course = driver.find_elements_by_class_name(
        "courseinfo__overviewtable__td")
    course_head = driver.find_elements_by_class_name(
        "courseinfo__overviewtable__th")

    # Dumps all data into a list
    course_data = data.add_elements_to_array(course)
    head_data = data.add_elements_to_array(course_head)

    # Formats all data for neater API output
    course_data = data.simpleFormatting(course_data)
    head_data = data.simpleFormattingHead(head_data)

    course_info = data.final_obj(head_data, course_data)

    driver.close()
    return course_info


def webscrape_all_sections(course_tag):
    driver = spawn_browser()
    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    course_list = driver.find_elements_by_link_text("Class Detail")

    list_data = []
    time.sleep(0.5)

    for i in range(len(course_list)):
        course_list[i].click()
        driver.implicitly_wait(3)
        course = driver.find_elements_by_class_name(
            "courseinfo__overviewtable__td")
        course_head = driver.find_elements_by_class_name(
            "courseinfo__overviewtable__th")

        course_data = data.add_elements_to_array(course)
        head_data = data.add_elements_to_array(course_head)

        course_data = data.simpleFormatting(course_data)
        head_data = data.simpleFormattingHead(head_data)

        course_info = data.final_obj(head_data, course_data)

        # print(head_data, file=sys.stderr)
        list_data.append(course_info)
        course_data = []
        head_data = []
        time.sleep(0.5)

    driver.close()
    return list_data
