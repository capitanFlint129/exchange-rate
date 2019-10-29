import aiohttp
import asyncio

rate = ""


async def update_rate(app):
    global rate
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.ratesapi.io/api/latest') as resp:
                    rate = await resp.text()
                    await asyncio.sleep(10)
        except aiohttp.ClientError:
            asyncio.sleep(0.5)

async def get_exchange_rate(request):
    global rate
    text = rate
    return aiohttp.web.Response(text=rate)
