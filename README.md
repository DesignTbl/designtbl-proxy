# designtbl-proxy
proxy image server

## Installation

This deploys automatically to heroku. Just push to a dyno.

To test locally, clone the repo and run:

```bash
python3 proxy.py
```

## Usage

Request a URL with a `src` query parameter that points to an image, e.g.

http://localhost:8000?src=https://some-url.com/some-image.jpg

optionally specify the `origin` parameter as well (defaults to `*`):

http://localhost:8000?origin=example.com&src=https://some-url.com/some-image.jpg



