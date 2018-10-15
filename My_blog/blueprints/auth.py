# -*- coding:utf-8 -*-
'''
 * @Author: SinTod
 * @Date: 2018-10-15 17:29:20
 * @Desc:
'''
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'The login page'


@auth_bp.route('/logout')
def logout():
    return 'Logout'
