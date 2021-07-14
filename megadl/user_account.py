# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae
# This plugin is working only if you Login with Mega Account

import json

from pyrogram import Client, filters
from pyrogram.types import Message
from hurry.filesize import size

from megadl.account import m
from config import Config

# Get Mega user Account info
@Client.on_message(filters.command("info") & filters.private)
async def nomegaurl(_, message: Message):
  if Config.USER_ACCOUNT == "False":
    await message.reply_text("You didn't setup a Mega.nz Account to Get details!")
    return
  get_user = m.get_user()
  imported_user = json.dumps(get_user)
  uacc_info = json.loads(imported_user)
  acc_email = uacc_info['email']
  acc_name = uacc_info['name']
  acc_quota = m.get_quota()
  acc_space_bytes = m.get_storage_space()
  # acc_space = size(acc_space_bytes)
  await message.reply_text(f"**Mega.nz User Account Info** \n\n**Account Name:** `{acc_name}` \n**Email:** `{acc_email}` \n**Storage Space:** `{acc_space_bytes}` \n**Quota:** `{acc_quota} MB`")
