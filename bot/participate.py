
from teleframework.shortcuts import *


participar_node = MenuNode(
  init=texts.participar,
  markup_scheme=(2, 1)
).add_options(
  (
    texts.participar_buttons_o,
    Redirect.create_go(['offer'])
  ),
  (
    texts.participar_buttons_n,
    Redirect.create_go(['demmand'])
  ),
  (
    texts.participar_buttons_cancelar,
    Redirect.create_back(2)
  )
)


participar_node.add_modules(
  'bot.offer',
  'bot.demmand'
)


