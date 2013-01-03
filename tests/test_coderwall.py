# coding=utf-8
from errbot.backends.test import FullStackTest, pushMessage, popMessage


class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super(TestCommands, cls).setUpClass(__file__)

    def test_coderwall(self):
        pushMessage('!coderwall gbin')
        self.assertIn('24PullRequests', popMessage())
        self.assertIn('Forked 20', popMessage())
