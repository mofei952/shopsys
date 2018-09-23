#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/22 13:19
# @File    : manager.py
# @Software: PyCharm

from flask_script import Server, Manager

from app import create_app

app = create_app()
manager = Manager(app)
server = Server(host="0.0.0.0", port=8001)
manager.add_command('runserver', server)


@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)


@manager.command
def test():
    pass


@manager.command
def deploy():
    pass


if __name__ == '__main__':
    manager.run()
