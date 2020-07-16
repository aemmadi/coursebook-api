# Import Libraries
# import data
import requests
import sys

from .data import *

# Renders raw markdown from README.md in github master branch into HTML


def docs_html():
    url = 'https://documentup.com/aemmadi/coursebook-api/__recompile'
    return f'<html><head><title>Unofficial API for UT Dallas Coursebook</title></head><body><h1><a href={url}>Documentation</a></h1></body></html>'

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


def grades_by_term(term):
    # Format to match data json
    term = convert_term(term)
    # course = convert_course(course)

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
    return grade_data
