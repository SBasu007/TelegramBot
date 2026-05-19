from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# ---------------- START COMMAND ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "HealthBot is active."
    )


# ---------------- TEXT MESSAGE ---------------- #

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    print("Message:", user_text)

    await update.message.reply_text(
        "Message received."
    )


# ---------------- FILE HANDLER ---------------- #

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):

    document = update.message.document

    file_name = document.file_name

    print("Received file:", file_name)

    # Create uploads folder if missing
    os.makedirs("uploads", exist_ok=True)

    # Get telegram file
    telegram_file = await document.get_file()

    # Save locally
    file_path = f"uploads/{file_name}"

    await telegram_file.download_to_drive(file_path)

    print("Saved to:", file_path)

    await update.message.reply_text(
        "Report received successfully."
    )


# ---------------- BOT SETUP ---------------- #

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT, handle_message)
)

app.add_handler(
    MessageHandler(filters.Document.ALL, handle_document)
)

print("Bot running...")

app.run_polling()