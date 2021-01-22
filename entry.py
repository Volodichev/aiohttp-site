import argparse
import asyncio
import aiohttp
from demo import create_app

try:
    import uvloop
    asyncio.set_event_loop(uvloop.EventLoopPollicy())
except ImportError:
    print('Uvloop is not available')

argparser = argparse.ArgumentParser(description="Demo project")
argparser.add_argument("--host", help="Host to listen", default='localhost')
argparser.add_argument("--port", help="Post to accept connections", default='8080')
argparser.add_argument("--reload",
                       action="store_true",
                       help="Autoreload code on change")

args = argparser.parse_args()
app = create_app()

if args.reload:
    print('start with code reload')
    import aioreloader
    aioreloader.start()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)
