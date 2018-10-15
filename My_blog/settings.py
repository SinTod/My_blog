# -*- coding:utf-8 -*-
'''
 * @Author: SinTod
 * @Date: 2018-10-15 17:14:46
 * @Desc:
'''
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

prefix = 'sqlite:////'

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data.db')

MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

BLOG_EMAIL = os.getenv('BLUELOG_EMAIL')
BLOG_POST_PER_PAGE = 10
BLOG_MANAGE_POST_PER_PAGE = 15
BLOG_COMMENT_PER_PAGE = 15
