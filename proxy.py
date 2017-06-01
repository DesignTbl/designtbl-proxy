#!/usr/bin/env python3
from sanic.app import Sanic
#from sanic.response import stream, file
import sanic.response as response
from urllib.parse import parse_qs
from sanic.log import log
import requests
import os
import requests
import shutil
from sanic.config import Config

Config.REQUEST_TIMEOUT = 10
app = Sanic()

@app.get('/')
async def cors(request):
    query = parse_qs(request.query_string)
    origin = query.get('origin')
    url = query.get('src')
    if not url:
        # you can serve a static page here
        return response.html(open('index.html').read())
    else:
        # query params return a list of values for each key
        url = url[0]
    if origin:
        origin = origin[0]
    else:
        origin = '*'
    image = requests.get(url, stream=True)
    image.raw.decode_content = True
    headers = dict()
    headers["Access-Control-Allow-Origin"] = origin
    headers["Access-Control-Allow-Credentials"] = True
    return response.raw(
        image.raw.read(),
        headers=headers,
        content_type=image.headers.get('Content-Type')
    )

app.run(
    host='0.0.0.0',
    port=os.environ.get('PORT') or 80,
    debug=True
)
