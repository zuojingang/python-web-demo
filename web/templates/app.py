#!/Users/zuojingang/python_venv/bin/python3.6
# -*- coding: utf-8 -*-
# @create_time: 2018-04-29 17:11:55
# @author  	:Jingang.Zuo

import logging
import asyncio
import sys
from aiohttp import web
sys.path.append("../../")
from src.common import db_conn

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=u'<h1>Awesome</h1>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    db_conn.create_pool(loop)
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
