#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: test_view_topic_posts.py
@time: 18-3-27 下午9:20
@version: v1.0 
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Post, Topic
from ..views import PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name="Django", description="Django boards")
        user = User.objects.create_user(username="tom", email="xiaohui100@gmial.com", password="1234567")
        topic = Topic.objects.create(subject="hellos", board=board, starter=user)
        Post.objects.create(message="hello Make", topic=topic, created_by=user)
        url = reverse("topic_posts", kwargs={"pk": board.pk, "topic_pk": topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEqual(view.func.view_class, PostListView)
