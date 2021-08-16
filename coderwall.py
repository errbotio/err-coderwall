import json
from urllib.error import HTTPError
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
        response = None
        username = args.strip()
        try:
            content = urlopen(f"http://coderwall.com/{username}.json")
            results = json.loads(content.read().decode())
            for badge in results["badges"]:
                self.send(mess.frm, BADGE % badge)
            response = USER % results
        except HTTPError:
            response = "User not found."
        return response
