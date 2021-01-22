from aiohttp import web
import aiohttp_jinja2 as aj
import jinja2

from .routes import setup_routes


async def create_app():
    app = web.Application()
    aj.setup(app,
             loader=jinja2.PackageLoader('demo', 'templates'))
    setup_routes(app)

    return app