import json
from urllib.request import urlopen

from errbot import BotPlugin, botcmd

USER = """
        User: %(username)s
        Name: %(name)s
        Team: %(team)s
    location: %(location)s
endorsements: %(endorsements)s
"""
BADGE = "%(name)20s -- %(description)s -- %(badge)s"


class Coderwall(BotPlugin):

    @botcmd
    def coderwall(self, mess, args):
        """Shows the badges of a coderwall user
        Example: !coderwall gbin
        """
        if not args:
            return "Am I supposed to guess the username?..."
        args = args.strip()
        content = urlopen("http://coderwall.com/%s.json" % args)
        results = json.loads(content.read().decode())
        for badge in results["badges"]:
            self.send(mess.frm, BADGE % badge)
        return USER % results
