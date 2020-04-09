
from teleframework.shortcuts import *

from json import dumps


with TeleFramework() as tf:
  tf.add_modules(
    'bot.root'
  )