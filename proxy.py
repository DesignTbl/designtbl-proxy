#!/usr/bin/env python3
from sanic.app import Sanic
from sanic.response import text
from urllib.parse import parse_qs
from sanic.log import log
import requests
import os
import requests
import shutil

app = Sanic()

@app.get('/')
def hello(request):
    query = parse_qs(request.query_string)
    url = query.get('src')[0]
    image = requests.get(url, stream=True)
    image.raw.decode_content = True
    return text(image.raw.read(), content_type=image.headers.get('Content-Type'))

app.run(
    host='0.0.0.0',
    port=os.environ.get('PORT')
)
