#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: test_view_board_topics.py
@time: 18-3-26 下午10:21
@version: v1.0 
"""
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import TopicListView
from ..models import Board


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django Board.")

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': '1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': '8'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
