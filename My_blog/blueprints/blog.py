# -*- coding:utf-8 -*-
'''
 * @Author: SinTod
 * @Date: 2018-10-15 17:33:14
 * @Desc:
'''
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/abuout')
def abuout():
    return 'The about page'


@blog_bp.route('category/<init:category_id>')
def category(category_id):
    return 'The category page'
