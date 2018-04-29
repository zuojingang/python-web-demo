#!/Users/zuojingang/python_venv/bin/python3.6
# -*- coding: utf-8 -*-
# @create_time: 2018-04-26 20:00:42
# @author  	:Jingang.Zuo

run_model = 'test'


config = {

    'develop': {
        'db': {
            'host': 'localhost',
            'port': 3306,
            'username': 'root',
            'password': 'test123',
            'database': 'python_demo_db'
        },
        'session': {
            'secret': ''
        }
    },


    'test': {
        'db': {
            'host': 'localhost',
            'port': 3306,
            'username': 'test',
            'password': 'test123',
            'database': 'python_demo_db'
        },
        'session': {
            'secret': ''
        }
    }
}


def config_attr(*args):
    ret_config = config.get(run_model)
    for arg in args:
        ret_config = ret_config.get(arg)
    return ret_config
