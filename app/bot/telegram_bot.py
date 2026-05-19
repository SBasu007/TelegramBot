from telegram import Update

from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

from dotenv import load_dotenv

import os

from app.agents.graph import (
    run_health_agent
)

load_dotenv()

BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    telegram_id = update.effective_user.id

    user_message = update.message.text

    response = run_health_agent(
        telegram_id,
        user_message
    )

    await update.message.reply_text(
        response
    )


app = ApplicationBuilder().token(
    BOT_TOKEN
).build()

app.add_handler(
    MessageHandler(
        filters.TEXT,
        handle_message
    )
)

print("Bot running...")

app.run_polling()