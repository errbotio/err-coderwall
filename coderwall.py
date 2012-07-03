from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd
import simplejson
from urllib2 import urlopen

USER = """\
        User: %(username)s
        Name: %(name)s
        Team: %(team)s
    location: %(location)s
endorsements: %(endorsements)s
"""
BADGE = '%(name)20s -- %(description)s -- %(badge)s'


class Coderwall(BotPlugin):
    min_err_version = '1.2.2'

    @botcmd
    def coderwall(self, mess, args):
        """ Shows the badges of a coderwall user
        Example: !coderwall gbin
        """
        if not args:
            return 'Am I supposed to guess the username?...'
        args = args.strip()
        content = urlopen('http://coderwall.com/%s.json' % args)
        results = simplejson.load(content)
        self.send(mess.getFrom(), USER % results, message_type=mess.getType())
        for badge in results['badges']:
            self.send(mess.getFrom(), BADGE % badge, message_type=mess.getType())
        return None
