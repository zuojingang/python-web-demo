#!/Users/zuojingang/python_venv/bin/python3.6
# -*- coding: utf-8 -*-
# @create_time: 2018-04-29 17:09:41
# @author  	:Jingang.Zuo

import logging
import aiomysql
import sys
sys.path.append("../")
from conf import _config
logging.basicConfig(level=logging.INFO)


async def create_pool(loop):
    '''
    doc test1
    '''
    logging.info('********** start create database connection pool **********')
    global __db_pool
    __db_pool = await aiomysql.create_pool(
        host=_config.config_attr('db', 'host'),
        port=_config.config_attr('db', 'port'),
        user=_config.config_attr('db', 'username'),
        password=_config.config_attr('db', 'password'),
        db=_config.config_attr('db', 'database'),
        charset='utf-8',
        autocommit=True,
        maxsize=10,
        minsize=1,
        loop=loop
    )


async def select(sql, args, size=None):
    '''
    doc test1
    '''
    logging.info(sql, args)
    global __db_pool
    async with __db_pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs


async def update(sql, args, autocommit=True):
    pass

