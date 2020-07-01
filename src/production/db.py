from pymongo import MongoClient
import os
import re
from .render import grades_by_term
from .data import *

# DEV ENVIRONMENT ONLY
from dotenv import load_dotenv
load_dotenv()

db = MongoClient(os.environ.get("DB_KEY"))
info_db = db.info
grades_db = db.grades
misc_db = db.misc
prof_db = db.prof


def get_single_course_grade(term, course, section):
    course = convert_course(course)
    subject = course[0].upper()
    number = course[1].upper()
    section = section.upper()

    grade_data = grades_db[term]
    course_grade = grade_data.find_one(
        {"subj": subject, "num": number, "sect": section})
    del course_grade["_id"]
    return course_grade


def get_all_course_grades(term, course):
    course = convert_course(course)
    subject = course[0].upper()
    number = course[1].upper()

    grade_data = grades_db[term]
    course_grades = list(grade_data.find({"subj": subject, "num": number}))
    course_grades = remove_id(course_grades)
    return course_grades


def fetch_prof(name):
    found_prof = list(prof_db["dir"].find(
        {"name": {"$regex": f"{name}", "$options": "i"}}))
    print(found_prof, file=sys.stderr)
    found_prof = remove_id(found_prof)
    return found_prof
