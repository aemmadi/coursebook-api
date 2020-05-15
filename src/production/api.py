# Import Libraries (heroku requires a . before local imports)
from flask import Flask, jsonify, render_template_string
from .scrape import webscrape, webscrape_all_sections
from .render import docs_html

# Configure as a flask server
app = Flask(__name__)

# Root endpoints only return README from github repo
@app.route('/')
@app.route('/v1/')
def render_docs():
    return render_template_string(docs_html())


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

    # Send response
    return jsonify({'data': class_info})

# GET /v1/<string: course>
@app.route('/v1/<string:course>/')
# Returns class data for all the sections in the current semester
def all_courses(course):
    course = course.lower()
    course_list = webscrape_all_sections(course)
    return jsonify({"data": course_list})


# Serve the server
if __name__ == '__main__':
    app.run(threaded=True)
