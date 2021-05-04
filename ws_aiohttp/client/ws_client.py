from aiohttp import ClientSession, WSMsgType
import asyncio


async def prompt_and_send(ws):
    new_msg_to_send = input("Type a message to send to the server: ")
    if new_msg_to_send == "exit":
        print("Exiting!")
        raise SystemExit(0)
    await ws.send_str(new_msg_to_send)


async def main():

    session = ClientSession()
    async with session.ws_connect("http://localhost:8000/ws") as ws:

        await prompt_and_send(ws)

        async for msg in ws:
            print("Message received from server:", msg)
            await prompt_and_send(ws)

            if msg.type in (WSMsgType.CLOSED, WSMsgType.ERROR):
                break


if __name__ == "__main__":
    print('Type "exit" to quit')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
