#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: test_form_signup.py.py
@time: 18-3-22 下午10:01
@version: v1.0 
"""

from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2', ]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
