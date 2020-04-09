
from teleframework.shortcuts import *

def info(ctx: BaseContext, chat_id: int = None):

  if not chat_id: chat_id = ctx.chat_id

  ctx.bot.send_message(
    chat_id=chat_id,

    text=texts.info_1
  )

  ctx.bot.send_message(
    chat_id=chat_id,

    text=texts.info_2
  )

  ctx.bot.send_photo(
    chat_id=chat_id,

    photo=texts.info_2_img
  )

  ctx.bot.send_message(
    chat_id=chat_id,

    text=texts.info_3
  )
  
  """
  ctx.bot.send_message(
    chat_id=chat_id,

    text=texts.info_4
  )
  """