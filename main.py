
from teleframework.shortcuts import *

from json import dumps

with TeleFramework(content_types=['text', 'photo']) as tf:
    
  tf.register_path(
    '',
    lambda ctx: ctx.send_msg(dumps(str(ctx.message)))
  )


  tf.add_modules(
    'bot.root'
  )