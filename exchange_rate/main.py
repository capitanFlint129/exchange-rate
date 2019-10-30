import asyncio
import logging

from aiohttp import web
from aiomisc.service.aiohttp import AIOHTTPService
from aiomisc import entrypoint
from aiomisc.log import basic_config

from routes import setup_routes
from views import update_rate

log = logging.getLogger(__name__)

basic_config(
    level=logging.INFO,
    log_format='color',
    buffered=False,
    buffer_size=1024,
)


async def start_background_tasks(app):
    app['rate_updater'] = asyncio.create_task(update_rate(app))
    log.info("Background task are created")


async def cleanup_background_tasks(app):
    app['rate_updater'].cancel()
    log.info("Background task are cancelled")
    await app['rate_updater']


class ExchangeRate(AIOHTTPService):
    async def create_application(self):
        app = web.Application()
        setup_routes(app)
        app.on_startup.append(start_background_tasks)
        app.on_cleanup.append(cleanup_background_tasks)
        log.info("Instance of app is created")
        return app

service = ExchangeRate(address="127.0.0.1", port=8080)

with entrypoint(service) as loop:
    log.info("Starting loop")
    loop.run_forever()
    log.info("Stopped")
