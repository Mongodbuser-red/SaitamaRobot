from typing import Optional, List

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.disable import DisableAbleCommandHandler

from telegraph import Telegraph, upload_file

@run_async
def media_telegraph(bot: Bot, update: Update):
    msg = update.effective_message # type: Optional[Message]


@run_async
def post_telegraph(bot: Bot, update: Update, args):
    short_name = "By @MaruyamaAya_bot"
    msg = update.effective_message # type: Optional[Message]
    telegraph = Telegraph()
    r = telegraph.create_account(short_name=short_name)
    auth_url = r["auth_url"]
    LOGGER.info(auth_url)
    title_of_page = " ".join(args)
    if title_of_page is "":
        title_of_page = 'By @MaruyamaAya_bot'
    page_content = msg.reply_to_message.text
    page_content = page_content.replace("\n", "<br>")
    response = telegraph.create_page(
        title_of_page,
        html_content=page_content
    )
    msg.reply_text("https://telegra.ph/{}".format(response["path"]))


__help__ = """- /teletext - <title of page > and reply to a long message
"""
__mod_name__ = "Telegraph"

dispatcher.add_handler(DisableAbleCommandHandler("teletext", post_telegraph, pass_args=True))
dispatcher.add_handler(DisableAbleCommandHandler("telemedia", media_telegraph, filters=Filters.video | Filters.photo))
