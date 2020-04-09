
from teleframework.shortcuts import *


participar_node = MenuNode(
  init=texts.participar,
  markup=(2, 1)
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
    Redirect.create_back()
  )
).register_path(
  'offer',
  Node().set_init_func(
    lambda ctx: (
      ctx.user.set_temp_name('ofrecimiento', []),
      Redirect.create_go(['add'])
    )
  ).register_path(
    'add',
    Redirect.create_go('choose'))
  ).register_path(
    'choose',
    ListNode(
      options_gen={
        opt: lambda ctx: (
          ctx.user.append_temp_name('ofrece', {'opcion': ctx.text}),
          Redirect.create_move(
            ['quantity']
          ) if opt != texts.participar_o_opts[-1] else 
          Redirect.create_go(
            ['other']
          )
        )[-1] for opt in texts.participar_o_opts
      },
      init=texts.participar_o,
      back=Redirect.create_back(2)
    ).register_path(
      'other',
      Node().set_init_func(
        lambda ctx: ctx.send_msg(texts.participar_o_otros, reply_markup=teletypes.ReplyKeyboardMarkup(teletypes.KeyboardButton(texts.back)))
      ).set_func(
        lambda ctx: (
          ctx.user.update_temp_name('ofrece', {'opcion': ctx.text}),
          Redirect.create_back() if ctx.text == texts.back else Redirect.create_go(['quantity'], 1)
        )[-1]
      )
    )
  ).register_path(
    f'quantity',
    FormNode(
      final=lambda ctx: (
        ctx.user.update_temp_name('ofrece', {'cantidad': ctx.params['answers'][0]}),
        Redirect.create_move()
      )[-1],
      back=Redirect.create_move(['choose'])
    ).add_questions(
      (
        texts.participar_o_cantidad,
        lambda ctx: False if ctx.text.isdigit() else texts.participar_o_cantidad_numero,
        lambda ctx: int(ctx.text)
      )
    )
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
      opt: lambda ctx: (
        ctx.user.update_temp_name('ofrece', {'opcion': ctx.text}),
        Redirect.create_move(
          ['quantity']
        ) if opt != texts.participar_o_opts[-1] else 
        Redirect.create_go(
          ['other']
        )
      )[-1] for opt in texts.participar_o_opts
    },
    init=texts.participar_o,
    back=Redirect.create_back(2)
  ).register_path(
    'other',
    Node().set_init_func(
      lambda ctx: ctx.send_msg(texts.participar_o_otros, reply_markup=teletypes.ReplyKeyboardMarkup(teletypes.KeyboardButton(texts.back)))
    ).set_func(
      lambda ctx: (
        ctx.user.update_temp_name('ofrece', {'opcion': ctx.text}),
        Redirect.create_back() if ctx.text == texts.back else Redirect.create_go(['quantity'], 1)
      )[-1]
    )
  )
).register_path(
  f'quantity',
  FormNode(
    final=lambda ctx: (
      ctx.user.update_temp_name('ofrece', {'cantidad': ctx.params['answers'][0]}),
      Redirect.create_move()
    )[-1],
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



