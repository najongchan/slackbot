from slacker import Slacker
import pytz
import random
import time
import github3
import datetime

localTimeZone = pytz.timezone('Asia/Seoul')
token = 'xoxb-347891948695-s3fUmvgxmBobgUeCIrckRBEi'
slack = Slacker(token)
username = '점심추천봇'
icon_emoji = ':dart:'
channel = ['#bottest', '#general', '#nago']
lunchlist = [u'굶기', u'다이어트']

attachement = {
    "pretext":"오늘의 점심은...?",
    "fallback":"점심추천봇",
    "text": lunchlist[random.randint(0, len(lunchlist) - 1)],
}

def poatMessage(channel, attachement, icon_emoji) :
    slack.chat.post_message(channel=channel, text=None, attachments=[attachement], icon_emoji=icon_emoji, as_user=False)

poatMessage(channel[0], attachement, icon_emoji)
