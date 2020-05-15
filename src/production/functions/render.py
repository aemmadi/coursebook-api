# Import Libraries
import requests

# Renders raw markdown from README.md in github master branch into HTML


def docs_html():
    url = 'https://api.github.com/markdown/raw'
    md = requests.get(
        'https://raw.githubusercontent.com/aemmadi/coursebook-api/master/README.md')
    html = requests.post(url, data=md.text, headers={
                         'Content-Type': 'text/x-markdown'})
    return f'<html><head><title>Unofficial API for UT Dallas Coursebook</title></head><body>{html.text}</body></html>'
