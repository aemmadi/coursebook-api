# Import Libraries
from flask import Flask, jsonify, render_template_string
from scrape_dev import *
from production.render import docs_html, get_grades
from production.db import *
import sys

# Configure as a flask server
app = Flask(__name__)

# Root endpoints only return README from github repo
@app.route('/')
@app.route('/v1/')
def render_docs():
    return render_template_string(docs_html())


# GET /v1/<string: term>/<string: course>/<string: section>


@app.route('/v1/<string:term>/<string:course>/<string:section>', methods=['GET'])
# Returns only the course requested
def single_course(term, course, section):
    # Formatting
    term = term.lower()
    course = course.lower()
    url = f"{course}.{section}.{term}"

    # Scrape coursebook
    class_info = webscrape_single_section(url)

    # Send response
    return jsonify({'data': class_info})

# GET /v1/<string: course>
@app.route('/v1/<string:course>/', methods=['GET'])
# Returns class data for all the sections in the current semester
def all_courses(course):
    course = course.lower()
    course_list = webscrape_all_sections(course)
    return jsonify({"data": course_list})


@app.route('/v1/grades/<string:term>/<string:course>/<string:section>', methods=['GET'])
def single_course_grade(term, course, section):
    grade_data = get_single_course_grade(term, course, section)
    return jsonify({"data": grade_data})


@app.route('/v1/grades/<string:term>/<string:course>', methods=['GET'])
def all_course_grades(term, course):
    grade_data = get_all_course_grades(term, course)
    return jsonify({"data": grade_data})


@app.route('/v1/prof/<string:name>', methods=['GET'])
def get_prof_data(name):
    prof_data = fetch_prof(name)
    return jsonify({"data": prof_data})


# Serve the server
if __name__ == '__main__':
    app.run(threaded=True)
