from linebot.models import TextSendMessage

from models import User
from models.status_type import StatusType
import const.message as ms


def self_ref(line_bot_api, user: User, event):
    text = event.message.text
    if text == ms.MSG_SELF_REF_1_EXP:
        user.set_session_type(StatusType.SELF_REF_EXP)
        user.set_session_stage(2)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=ms.MSG_SELF_REF_EXP_1))
        line_bot_api.push_message(user.get_id(), TextSendMessage(text=ms.MSG_SELF_REF_EXP_1_EX))
    elif text == ms.MSG_SELF_REF_1_PERS:
        user.set_session_type(StatusType.SELF_REF_PERS)
        user.set_session_stage(2)
        pass
    elif text == ms.MSG_SELF_REF_1_VIS:
        user.set_session_type(StatusType.SELF_REF_VIS)
        user.set_session_stage(2)
        pass
    elif text == ms.MSG_SELF_REF_1_TURN:
        user.set_session_type(StatusType.SELF_REF_TURN)
        user.set_session_stage(2)
        pass