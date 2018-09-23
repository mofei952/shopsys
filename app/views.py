#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/22 13:18
# @File    : views.py
# @Software: PyCharm
import json

from flask import render_template, request


def init_app(app):
    @app.route('/upload')
    def upload():
        pass

    @app.route('/')
    def index():
        from app.model import Commodity
        commodity_list = Commodity.query.all()
        return render_template('index.html', commodity_list=commodity_list)

    @app.route('/test')
    def test():
        return render_template('index.html')

    @app.route('/admin/')
    def admin_index():
        return render_template('admin/index.html')

    @app.route('/admin/commodity_list')
    def admin_commodity_list():
        from app.model import Commodity
        commodity_list = Commodity.query.all()
        return render_template('admin/commodity_list.html', commodity_list=commodity_list)

    def next_commodity_number():
        return 'xx00000001'

    @app.route('/admin/add_commodity')
    def admin_add_commodity():
        # 生成默认货号
        number = next_commodity_number()
        # 查询所有分类
        from app.model import Category
        category_list = Category.query.all()
        return render_template('admin/add_commodity.html', number=number, category_list=category_list)

    @app.route('/admin/commodity_category')
    def admin_commodity_category():
        from app.model import Category
        category_list = Category.query.all()
        return render_template('admin/commodity_category.html', category_list=category_list)

    @app.route('/admin/add_category', methods=['GET', 'POST'])
    def admin_add_category():
        if request.method == 'GET':
            return render_template('admin/add_category.html')
        else:
            from app.model import Category
            from app import db
            name = request.form['name']
            db.session.add(Category(name=name))
            db.session.commit()
            return json.dumps({'success': True})
