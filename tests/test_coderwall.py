from errbot.backends.test import FullStackTest, popMessage, pushMessage


class TestCommands(FullStackTest):
    def test_coderwall(self):
        pushMessage("!coderwall gbin")
        self.assertIn("24PullRequests", popMessage())
        self.assertIn("Forked", popMessage())
