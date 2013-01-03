from errbot import botcmd, BotPlugin, PY2

import json
if PY2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

USER = """
        User: %(username)s
        Name: %(name)s
        Team: %(team)s
    location: %(location)s
endorsements: %(endorsements)s
"""
BADGE = '%(name)20s -- %(description)s -- %(badge)s'


class Coderwall(BotPlugin):
    min_err_version = '1.6.0'

    @botcmd
    def coderwall(self, mess, args):
        """ Shows the badges of a coderwall user
        Example: !coderwall gbin
        """
        if not args:
            return 'Am I supposed to guess the username?...'
        args = args.strip()
        content = urlopen('http://coderwall.com/%s.json' % args)
        results = json.loads(content.read().decode())
        for badge in results['badges']:
            self.send(mess.getFrom(), BADGE % badge, message_type=mess.getType())
        return USER % results
