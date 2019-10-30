import logging
import asyncio

import aiohttp

log = logging.getLogger(__name__)

rate = ""


async def update_rate(app):
    global rate
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                log.info("Get session")
                async with session.get('https://api.ratesapi.io/api/latest') as resp:
                    log.info("Exchange rate request made")
                    rate = await resp.text()
                    log.info("Exchange rate updated")
                    await asyncio.sleep(10)
        except aiohttp.ClientError:
            log.exception("Unable to get exchange rate")
            asyncio.sleep(0.5)

async def get_exchange_rate(request):
    global rate
    text = rate
    log.info("Successfully responded to a currency rate request")
    return aiohttp.web.Response(text=rate)
