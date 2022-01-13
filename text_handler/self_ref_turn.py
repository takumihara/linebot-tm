from linebot.models import TextSendMessage

import message as ms
import line


def self_ref_turn(line_bot_api, user, event):
    ss_stage = user.get_session_stage()
    text = event.message.text
    if text == ms.default.KEY_NEXT:
        msg = _route_next(user)
        if msg:
            line.reply_msg(line_bot_api, event, msg)
            if ss_stage not in (7,):
                line_bot_api.push_message(user.get_id(), TextSendMessage(text=ms.default.ASK_FOR_NEXT))


def _route_next(user):
    ss_stage = user.get_session_stage()
    msg = None
    if ss_stage == 2:
        msg = ms.self_ref.TURN_2
    if ss_stage == 3:
        msg = ms.self_ref.TURN_3
    elif ss_stage == 4:
        msg = ms.self_ref.TURN_4
    elif ss_stage == 5:
        msg = ms.self_ref.TURN_5
    elif ss_stage == 6:
        msg = ms.self_ref.TURN_6
    if msg:
        user.increment_session_stage()
        return msg
    if ss_stage == 7:
        user.reset()
        return ms.default.END