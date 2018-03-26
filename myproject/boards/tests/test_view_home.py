#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: test_view_home.py
@time: 18-3-26 下午10:21
@version: v1.0 
"""
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home
from ..models import Board


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

