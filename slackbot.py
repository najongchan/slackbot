from slacker import Slacker
import pytz
import github3
import datetime

localTimeZone = pytz.timezone('Asia/Seoul')
token = 'xoxb-347891948695-mU7krv7r2hIMJsz5u5aAMhyn'
slack = Slacker(token)
channel = ['#bottest', '#general', '#nago']

def poatMessage(channel, message) :
    slack.chat.post_message(channel, message, as_user=True)

