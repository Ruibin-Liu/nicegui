
from nicegui import Client, ui


def log(msg: str):
    print(msg, flush=True)
    with open('output.log', 'a') as f:
        f.write(msg)


@ui.page('/')
async def page(client: Client):
    log('loading')
    await client.connected()
    log('connected')
    result = await ui.run_javascript('return "Roundtrip works!"')
    log(result)


ui.run(reload=False, native=True)
