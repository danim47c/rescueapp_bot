
from teleframework.shortcuts import *


participar_node = MenuNode(
  init=texts.participar,
  markup=(2, 1)
).add_options(
  (
    texts.participar_buttons_o,
    Redirect.create_go(['ofrecer'])
  ),
  (
    texts.participar_buttons_n,
    Redirect.create_go(['necesitar'])
  ),
  (
    texts.participar_buttons_cancelar,
    Redirect.create_back()
  )
)


participar_o_node = Node()

@participar_o_node.init_func_decorator()
def participar_o_node_init_func(ctx: BaseContext):
  ctx.user.set_temp_name('ofrece', [])
  return Redirect.create_go(['add'])

participar_o_node.register_path(
  'add',
  Node().set_init_func(lambda ctx: Redirect.create_go('choose'))
).register_path(
  'choose',
  ListNode(
    options_gen={
      opt: (
        Redirect.create_move(
          [f'quantity?opt={opt}']
        ) if opt != texts.participar_o_opts[-1] else 
        Redirect.create_go(
          ['other']
        )
      ) for opt in texts.participar_o_opts
    },
    init=texts.participar_o,
    back=Redirect.create_back(2)
  ).register_path(
    'other',
    Node().set_init_func(
      lambda ctx: ctx.send_msg(texts.participar_o_otros, reply_markup=teletypes.ReplyKeyboardMarkup(teletypes.KeyboardButton(texts.back)))
    ).set_func(
      lambda ctx: Redirect.create_back() if ctx.text == texts.back else Redirect.create_go([f'quantity?opt={ctx.text}'], 1)
    )
  )
).register_path(
  f'quantity',
  FormNode(
    final=lambda ctx: None,
    back=Redirect.create_move(['choose'])
  ).add_questions(
    (
      texts.participar_o_cantidad,
      lambda ctx: False if ctx.text.isdigit() else texts.participar_o_cantidad_numero,
      lambda ctx: int(ctx.text)
    )
  )
)






participar_n_node = None



