# ws_aiohttp

A simple websocket client and server implemented by using (aiohttp)[https://docs.aiohttp.org/] framework.

Requirements:
- [poetry](https://pypi.org/project/poetry/)
- [aiohttp-devtools](https://pypi.org/project/aiohttp-devtools/)

To start server:
```
% cd server
% poetry install
% poetry run adev runserver .
```

Sanity check the server from another shell:
```
% curl -i http://localhost:8000
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 14
Server: Python/3.9 aiohttp/3.7.4.post0

Hello, world!
```

To start the client, open up another shell:
```
% cd client
% poetry install
% poetry run python ws_client.py
```
