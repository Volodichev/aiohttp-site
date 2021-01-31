from aiohttp import web
import aiohttp_jinja2 as aj
import jinja2
import asyncpgsa

from .routes import setup_routes


async def create_app(config:dict):
    app = web.Application()
    app['config'] = config
    aj.setup(app,
             loader=jinja2.PackageLoader('demo', 'templates'))
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_shutdown.append(on_shutdown)
    return app

async def on_start(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['datebase_url'])


async def on_shutdown(app):
    await app['db'].close()


