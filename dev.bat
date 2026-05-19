@echo off
echo Starting bot with auto-reload...
set PYTHONPATH=%CD%
watchmedo auto-restart --directory=./app/bot --pattern="*.py" --recursive -- python app/bot/telegram_bot.py
