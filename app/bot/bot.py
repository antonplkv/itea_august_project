import json
from .config import TOKEN, CATEGORY_TAG
from .keyboards import START_KB
from .utils import check_message_match, check_call_tag_match, generate_categories_kb
from .texts import GREETINGS, PICK_CATEGORY
from ..models.models import Category
from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(button) for button in START_KB.values()]
    kb.add(*buttons)
    bot.send_message(
        message.chat.id,
        GREETINGS,
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: check_message_match(m, 'category'))
def show_categories(message):
    kb = generate_categories_kb(Category.get_root_categories())
    bot.send_message(
        message.chat.id,
        PICK_CATEGORY,
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda c: check_call_tag_match(c, CATEGORY_TAG))
def category(call):
    category = Category.objects.get(id=json.loads(call.data)['id'])

    if category.subcategories:
        kb = generate_categories_kb(category.subcategories)
        bot.edit_message_text(
            category.title,
            call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=kb
        )
    else:
        for product in category.get_products():
            bot.send_photo(
                call.message.chat.id,
                product.image.read(),
                caption=product.get_formatted_text()

            )