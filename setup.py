#!/Users/zuojingang/python_venv/bin/python3.6
# -*- coding: utf-8 -*-
# @create_time: 2018-04-29 22:09:47
# @author  	:Jingang.Zuo

from setuptools import setup, find_packages

setup(
    name='python-web-demo',
    version='1.0',
    author='Jingang.Zuo',
    author_email='',
    url='http://python-web-demo.readthedocs.io/en/latest/index.html',
    description='Demo of python',
    long_description='Demo of python',
    # platforms=['Linux', 'MacOS', 'Windows'],
    packages=[''],
    # py_modules=[],
    download_url='https://github.com/zuojingang/python-web-demo/archive/master.zip',
    # data_files=[],
    # scripts=[],
    package_dir={'': 'src'},
    # requires=[],
    # provides=[],
    # packages=find_packages(
    # exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    # ),
    install_requires=[
        'aiohttp>=3.1.3',
        'aiomysql>=0.0.14',
        'Jinja2>=2.10'
    ],
    # entry_points={'console_scripts': [
    #         'redis_run = RedisRun.redis_run:main',
    # ]},
    # zip_safe=False
)
