import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import CommandHandler, InlineQueryHandler, Updater
from telegram.utils.helpers import escape_markdown

from . import cow
from .settings import BOT_TOKEN


logger = logging.getLogger(__name__)


def make_result_article(title: str, text: str):
    content = InputTextMessageContent(
        f"```{text}```",
        parse_mode=ParseMode.MARKDOWN
    )
    return InlineQueryResultArticle(
        id=uuid4(),
        title=title,
        input_message_content=content
    )


def inline_query(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    # todo: extract parameters from query
    text = query
    text = escape_markdown(text)
    text = cow.make_message(text)

    results = [
        make_result_article('Cow', text)
    ]
    update.inline_query.answer(results)


def start(_, update):
    update.reply_text('Moo 🐮')


def error(_, update, err):
    logger.warning('Update "%s" caused error "%s"', update, err)


def run():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(InlineQueryHandler(inline_query))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
