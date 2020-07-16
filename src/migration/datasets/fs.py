from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

db = MongoClient(os.environ.get("DB_KEY"))
grades_db = db.grades

# course_set = set()
# terms = ["17f", "18f", "18s", "19f", "19s", "20s"]

# for term in terms:
#     print(term)
#     term_db = grades_db[term]
#     term_arr = term_db.find({}, ['subj', 'num'])
#     for course in term_arr:
#         number = f'{course["subj"]}{course["num"]}'
#         course_set.add(number)

# tmp = []
misc_db = db.misc
# misc_col = misc_db["class_list"]
# print(misc_col.find_one({"course": "CS4337"})["scanned_on"])
# for course in course_set:
#     now = datetime.now()
#     obj = {'course': course, 'scanned_on': now}
#     tmp.append(obj)

# print(tmp)
# misc_col.insert_many(tmp)

prof_data = []


def update_prof_list_from_txt(file):
    f = open(file)
    for i in range(1767):
        prof_data.append({"name": f.readline()[:-1]})
    misc_col = misc_db["prof_list"]
    misc_col.insert_many(prof_data)


update_prof_list_from_txt("prof.txt")
