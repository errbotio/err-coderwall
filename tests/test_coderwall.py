# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):

    def test_coderwall(self):
        pushMessage('!coderwall gbin')
        self.assertIn('24PullRequests', popMessage())
        self.assertIn('Forked', popMessage())
