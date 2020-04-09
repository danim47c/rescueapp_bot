
from teleframework.shortcuts import *

from bot.info import info

from bot.participate import participar_node

def start_command(ctx: BaseContext):

  return info(ctx)



def setup(tf: TeleFramework):

  tf.register_command(
    '/start',
    start_command
  )

  tf.register_command(
    '/participar',
    participar_node
  )



