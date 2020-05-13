# Import Libraries
from flask import Flask, jsonify
from scrape_dev import webscrape

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
    class_info = webscrape(url)

    # Seperate into two parallel arrays
    classData = class_info['data']
    classHead = class_info['head']

    # Basic formatting of raw data for a neater API
    classData = simpleFormatting(classData)
    classHead = simpleFormattingHead(classHead)

    # Send response
    return jsonify({
        'data': final_obj(classHead, classData)
    })

# Converts the raw data into a neat API output


def simpleFormatting(data):
    for i in range(len(data)):
        if '\n' in data[i]:
            data[i] = data[i].split('\n')  # Create sub list
        if '    ' in data[i]:
            data[i] = data[i].split("    ")  # Create sub list
        if '   ' in data[i]:
            data[i] = data[i].split("   ")  # Create sub list

    # Hardcoded sub lists (Guaranteed in every scrape)
    data[1][0] = data[1][0].split(" Instruction ")
    data[1][1] = data[1][1].split(" Activity ")
    data[1][2] = data[1][2].split(" Class/")
    data[1][3] = data[1][3].split(" Session ")
    data[1][4] = data[1][4].split(" Orion ")

    return data

# Converts the raw data into a neat API output


def simpleFormattingHead(head):
    for i in range(len(head)):
        if ':' in head[i]:
            head[i] = head[i].replace(':', '')
        if '(s)' in head[i]:
            head[i] = head[i].replace('(s)', '')
        if ' ' in head[i]:
            head[i] = head[i].replace(' ', '_')
    return head

# Combines two parallel arrays into a single object


def final_obj(head, data):
    final = {}
    for i in range(len(head)):
        final.update({head[i].lower(): data[i]})
    return final


# Serve the server
if __name__ == '__main__':
    app.run(threaded=True)
