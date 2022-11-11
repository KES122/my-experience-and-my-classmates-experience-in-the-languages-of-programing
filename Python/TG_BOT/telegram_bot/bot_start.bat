@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5324746423:AAGp64S256cIW8Hmwv3JxHKmLvp3V-5dteI

python bot_telegram.py

pause