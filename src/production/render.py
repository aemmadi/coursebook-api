# Import Libraries
import requests
import re
import sys

# Renders raw markdown from README.md in github master branch into HTML


def docs_html():
    url = 'https://api.github.com/markdown/raw'
    md = requests.get(
        'https://raw.githubusercontent.com/aemmadi/coursebook-api/master/README.md')
    html = requests.post(url, data=md.text, headers={
                         'Content-Type': 'text/x-markdown'})
    return f'<html><head><title>Unofficial API for UT Dallas Coursebook</title></head><body>{html.text}</body></html>'

# Retrieves grades from utd-grades github repo


def get_grades(term, course, section):
    # Format to match data json
    term = convert_term(term)
    course = convert_course(course)

    # Bad input
    if(term == -1):
        return 400

    # Find json for term
    url = f'https://api.github.com/repos/bharatari/utd-grades/contents/data/{term}?ref=master'
    response = requests.get(url).json()

    for raw_file in response:
        if "json" in raw_file["name"]:
            url = raw_file["download_url"]

    # Grab json
    grade_data = requests.get(url).json()

    # Parse and return requested data
    for i in range(len(grade_data)):
        if grade_data[i]["subj"].lower() == course[0].lower():
            if grade_data[i]["num"] == course[1]:
                if grade_data[i]["sect"].lower() == section.lower():
                    return grade_data[i]


# Converts course into an array seperating subject and number, math2413 -> [math, 2413]

def convert_course(course):
    num = re.findall('\d+', course)[0]
    subj = course.replace(f"{num}", "")
    return [subj, num]

# Converts term into expanded format, 18f -> Fall 2018


def convert_term(term):
    season = term[-1]
    term = f"20{term[:-1]}"

    if season == "f":
        season = "Fall"
    elif season == "s":
        season = "Spring"
    elif season == "u":
        season = "Summer"
    else:
        return -1

    return f"{season}%20{term}"
