import logging
import telebot
from database import limit_users, check_user_in_db, create_table, insert_data
from config import bot_token
from validators import is_stt_block_limit
from info import bot_templates
from speechApi import send_request

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, bot_templates['say_start'])
    create_table()

    user_id = message.from_user.id
    limit = limit_users()
    checked_user = check_user_in_db(user_id)

    if limit and not checked_user:
        bot.send_message(message.chat.id, bot_templates['user_limit'])
    else:
        insert_data(user_id)


@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.chat.id, bot_templates['say_help'])


@bot.message_handler(commands=['stt'])
def stt_handler(message):
    user_id = message.from_user.id
    checked_user = check_user_in_db(user_id)
    if checked_user:
        bot.send_message(message.chat.id, bot_templates['say_generate'])
        bot.register_next_step_handler(message, speech_to_text)
    else:
        bot.send_message(message.chat.id, bot_templates['hard_user_limit'])


def speech_to_text(message):
    user_id = message.from_user.id

    if not message.voice:
        bot.send_message(message.chat.id, bot_templates['if_not_voice'])

    else:
        blocks, msg = is_stt_block_limit(message, message.voice.duration)

        if not blocks:
            bot.send_message(message.chat.id, msg)

        else:
            file_id = message.voice.file_id
            file_info = bot.get_file(file_id)
            file = bot.download_file(file_info.file_path)
            status, text = send_request(file)

            if status:
                insert_data(user_id, message.text, blocks)
                bot.send_message(message.chat.id, text, reply_to_message_id=message.id)
                logging.info("Аудиофайл успешно переработан в текст.")
            else:
                logging.error("Ошибка:", text)

    bot.register_next_step_handler(message, speech_to_text)


@bot.message_handler(commands=['debug'])
def send_logs(message):
    with open("log_file.txt", "rb") as f:
        bot.send_document(message.chat.id, f)
        logging.info("Use command DEBUG")


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, bot_templates['for_text'])


bot.infinity_polling()