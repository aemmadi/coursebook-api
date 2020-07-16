# Import Libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from production.data import *
import sys

# Configure chromedriver
opt = Options()
# opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--no-sandbox")
driver = webdriver.Chrome("bin/chromedriver-mac", chrome_options=opt)
driver.get("https://coursebook.utdallas.edu")


def spawn_browser():
    spawn = webdriver.Chrome("bin/chromedriver-win.exe", chrome_options=opt)
    return spawn


# Scrape coursebook, given the formatted course tag (Ex: cs4337.001.20f)

def webscrape_single_section(course_tag):
    driver.get(
        f"https://coursebook.utdallas.edu/clips/clip-coursebook.zog?id={course_tag}&action=info")

    course = set_inject_vars(driver)["course"]
    course_head = set_inject_vars(driver)["course_head"]

    course_info = scrape_data(course, course_head)
    course_info = array_to_obj(course_info)
    return course_info

# Scrape all sections for a course on coursebook


def webscrape_all_sections(course_tag):
    driver.get(f"https://coursebook.utdallas.edu/search/{course_tag}")
    course_list = driver.find_elements_by_class_name("stopbubble")
    current_term = driver.find_element_by_class_name("directaddress").text

    course_list = add_elements_to_array(course_list)
    course_list = course_list
    current_term = current_term[-3:]
    list_data = []

    for course in course_list:
        list_data.append(webscrape_single_section(
            f"{course.replace(' ', '').lower()}.{current_term}"))
        time.sleep(0.2)

    return list_data


def scrape_prof_data(prof_list):
    success = []
    failed = []
    for prof in prof_list:
        # prof = prof_list[0]
        try:
            driver.get(
                f"https://www.utdallas.edu/directory/includes/directories.class.php?dirType=displayname&dirSearch={prof['name']}&dirAffil=faculty&dirDept=All&dirMajor=All&dirSchool=All")
            name = driver.find_element_by_class_name("fullname").text
            details = driver.find_element_by_class_name("output").text
            # print(name, file=sys.stderr)
            details = details.split("\n")
            details[4] = details[4].replace("Office - ", "")
            details[5] = details[5].replace("Mailstop - ", "")

            success.append({"name": name, "email": details[0], "title": details[1], "department": details[2],
                            "phone": details[3], "office": details[4], "mailstop": details[5]})
        except:
            # print(f"ERROR {prof['name']}", file=sys.stderr)
            failed.append(prof['name'])
    return {
        'success': success,
        'failed': failed
    }


def set_inject_vars(driver):
    return {"course": driver.find_elements_by_class_name(
            "courseinfo__overviewtable__td"),
            "course_head": driver.find_elements_by_class_name(
            "courseinfo__overviewtable__th")}
