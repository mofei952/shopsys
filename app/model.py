#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/22 12:52
# @File    : model.py
# @Software: PyCharm

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)
    attr = db.Column(db.Text)
    stock_count = db.Column(db.Integer)
    stock_warning_count = db.Column(db.Integer)
    is_sell = db.Column(db.Boolean)
    carousel_images = db.Column(db.Text, nullable=False)
    detail = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='commodities')

# class ShoppingCartCommodity(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user = db.Column(db.Integer, db.ForeignKey('user.id'))
#     commodity = db.Column(db.Integer, db.ForeignKey('commodity.id'))
#
#
# class OrderForm(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
#
# class OrderCommodity(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_form_id = db.Column(db.Integer, db.ForeignKey('order_form_id'))
#
#
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
