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

app = Sanic()

@app.get('/')
async def hello(request):
    query = parse_qs(request.query_string)
    url = query.get('src')
    if not url:
        return response.text("OK", status_code=200)
    else:
        # query params return a list of values for each key
        url = url[0]
    image = requests.get(url, stream=True)
    image.raw.decode_content = True
    # we could consider caching the images by url
    return response.raw(
        image.raw.read(),
        content_type=image.headers.get('Content-Type')
    )

app.run(
    host='0.0.0.0',
    port=os.environ.get('PORT')
)
