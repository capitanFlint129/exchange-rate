from aiohttp import web
from routes import setup_routes
from views import update_rate
from aiomisc import AIOHTTPService, entrypoint
import asyncio


async def start_background_tasks(app):
    app['rate_updater'] = asyncio.create_task(update_rate(app))


async def cleanup_background_tasks(app):
    app['rate_updater'].cancel()
    await app['rate_updater']


class ExchangeRate(AIOHTTPService):
    async def create_application(self):
        app = web.Application()
        setup_routes(app)
        app.on_startup.append(start_background_tasks)
        app.on_cleanup.append(cleanup_background_tasks)
        return app

service = ExchangeRate(address="127.0.0.1", port=8080)

with entrypoint(service) as loop:
    loop.run_forever()
