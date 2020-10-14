import json

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from .config import CATEGORY_TAG
from .keyboards import START_KB


def check_message_match(message, text):
    return message.text == START_KB[text]


def check_call_tag_match(call, tag):
    return json.loads(call.data)['tag'] == tag


def generate_categories_kb(categories_qs):
    buttons = []
    kb = InlineKeyboardMarkup()
    for c in categories_qs:
        data = json.dumps(
            {
                'id': str(c.id),
                'tag': CATEGORY_TAG
            }
        )
        buttons.append(InlineKeyboardButton(c.title, callback_data=data))
    kb.add(*buttons)
    return kb