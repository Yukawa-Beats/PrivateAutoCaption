#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) Yukawa Beats

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME

@Client.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""<b> 👋ഹെലോ🙋🏻‍♂️ {update.from_user.mention}\n\nഞാൻ ഒരു ഓട്ടോ ക്യാപ്ഷൻ ബോട്ട് ആണ്🤩🤩എന്നെ ഉണ്ടാക്കിയത് @chekuthan_0405 ആണ്..👑\n\nഎന്നെ നിങ്ങളുടെ ചാനലിൽ ആഡ് ആക്ക്..പിന്നെ എന്റെ പവർ ഞാൻ കാണിച്ചു തരാം..🤪🤪\n\nബോട്ട് ക്രിയേറ്ററുടെ ചാനലിൽ ജോയിൻ ആവുക..👉 @ybdemochannel 💃🏻🕺🏻\n\n© @chekuthan_0405</b>"""
    reply_markup =  InlineKeyboardMarkup(
                                         [[
        InlineKeyboardButton("help ↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️ Group", url="t.me/ybmoviesgroup"),
        InlineKeyboardButton("Channel 📢", url="t.me/ybdemochannel")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🖥️ YouTube 🖥️", url="https://youtube.com/channel/UCnI4WI9dFLez9GmMi54EyEA")
            ],[
            InlineKeyboardButton("Home 🏠", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("Close ❌️", callback_data="motech"),
            InlineKeyboardButton("About ↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>🔻Auto Caption Bot🔻\n\nഎഡിറ്റ് ചെയ്യാൻ വേണ്ടി Heroku അക്കൗണ്ടിൽ പോകുക👇\n\nHeroku 👉 https://dashboard.heroku.com\n\n© Yukawa Beats</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="t.me/ybmoviesgroup"),
            InlineKeyboardButton("Channel📢", url="t.me/ybdemochannel"),
            ],[
            InlineKeyboardButton("Home 🏠", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("Back 🔙", callback_data="heroku"),
            InlineKeyboardButton("Close ❌️", callback_data="motech")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> Auto Caption Bot\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : Heroku</b> \n\n<b>➪ Version : 2.0.1</b>\n\n<b>➪ Source Code  : <a href="https://github.com/Yukawa-Beats/PrivateAutoCaption">Touch Me 🤗</a>\n\n➪ Developer :  *Yukawa Beats* \n\n➪ Credits : <a href="https://instagram.com/yukawa_beats">Credits</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
