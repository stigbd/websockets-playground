"""Package for exposing validation endpoint."""
from aiohttp import web, WSMsgType


async def hello(request):
    """Add a Hello world route for sanity's sake."""
    return web.Response(text="Hello, world!\n")


async def websocket_handler(request):
    """Set up the websocket connection."""

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == "close":
                await ws.close()
            else:
                await ws.send_str(msg.data + "/answer")
        elif msg.type == WSMsgType.ERROR:
            print("ws connection closed with exception %s" % ws.exception())

    print("websocket connection closed")

    return ws


async def create_app() -> web.Application:
    """Create a web application."""
    app = web.Application()
    app.add_routes(
        [
            web.view("/", hello),
            web.get("/ws", websocket_handler),
        ]
    )

    return app
