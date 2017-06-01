#!/usr/bin/env python3
from sanic.app import Sanic
#from sanic.response import stream, file
from sanic.response import raw, html
from urllib.parse import parse_qs
from sanic.log import log
import requests
import aiohttp
import os
import requests
import shutil
from sanic.config import Config
import asyncio
import async_timeout

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.read(), response.headers

Config.REQUEST_TIMEOUT = 10
app = Sanic()

@app.get('/')
async def cors(request):
    query = parse_qs(request.query_string)
    origin = query.get('origin')
    url = query.get('src')
    if not url:
        # you can serve a static page here
        return html(open('index.html').read())
    else:
        # query params return a list of values for each key
        url = url[0]
    if origin:
        origin = origin[0]
    else:
        origin = '*'
    async with aiohttp.ClientSession(loop=asyncio.get_event_loop()) as session:
        response = await fetch(session, url)
    headers = dict()
    headers["Access-Control-Allow-Origin"] = origin
    headers["Access-Control-Allow-Credentials"] = True
    return raw(
        response[0],
        headers=headers,
        content_type=response[1].get('Content-Type')
    )

app.run(
    host='0.0.0.0',
    port=os.environ.get('PORT') or 80,
    debug=True
)
