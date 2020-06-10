# Import Libraries
import requests
import sys

# Renders raw markdown from README.md in github master branch into HTML


def docs_html():
    url = 'https://api.github.com/markdown/raw'
    md = requests.get(
        'https://raw.githubusercontent.com/aemmadi/coursebook-api/master/README.md')
    html = requests.post(url, data=md.text, headers={
                         'Content-Type': 'text/x-markdown'})
    return f'<html><head><title>Unofficial API for UT Dallas Coursebook</title></head><body>{html.text}</body></html>'


def get_grades(term, course, section):
    url = 'https://api.github.com/repos/bharatari/utd-grades/'
    term = convert_term(term)
    return term


def convert_term(term):
    season = term[-1]
    term = term[:-1]
    print(season, file=sys.stderr)
    return [season, term]
