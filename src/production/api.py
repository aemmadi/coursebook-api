# Import Libraries
from flask import Flask, jsonify
from .scrape import webscrape  # .scrape for heroku deployment
import re

# Configure as a flask server
app = Flask(__name__)

# GET /v1/<string: term>/<string: course>/<string: section>


@app.route('/v1/<string:term>/<string:course>/<string:section>')
# Returns only the course requested
def perma_course(term, course, section):
    # Formatting
    term = term.lower()
    course = course.lower()
    url = f"{course}.{section}.{term}"

    # Scrape coursebook
    classData = webscrape(url)

    # Basic formatting of raw data for a neater API
    classData = simpleFormatting(classData)

    # Send response
    return jsonify({
        'class_title': classData[0],
        'class_info': classData[1],
        'class_status': classData[2],
        'class_desc': classData[3],
        'class_attr': classData[4],
        'class_reqs': classData[5],
        'class_instructor': classData[6],
        'class_ta': classData[7],
        'class_schedule': classData[8],
        'class_crosslist': classData[9],
        'class_college': classData[10],
        'class_syllabus': classData[11],
        'class_eval': classData[12]
    })

# Converts the raw data into a neat API output


def simpleFormatting(data):
    for i in range(len(data)):
        if '\n' in data[i]:
            data[i] = data[i].split('\n')  # Create sub list
        if '  ' in data[i]:
            data[i] = data[i].split("    ")  # Create sub list

    # Hardcoded sub lists (Guaranteed in every scrape)
    data[1][0] = data[1][0].split(" Instruction ")
    data[1][1] = data[1][1].split(" Activity ")
    data[1][2] = data[1][2].split(" Class/")
    data[1][3] = data[1][3].split(" Session ")
    data[1][4] = data[1][4].split(" Orion ")

    return data


# Serve the server
if __name__ == '__main__':
    app.run(threaded=True)
