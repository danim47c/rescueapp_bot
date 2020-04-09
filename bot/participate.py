
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
).register_path(
  'offer',
  Node().set_init_func(
    lambda ctx: (
      offer := Offer.create(user=ctx.user),
      Redirect.create_go([f'add?another=False&oid={offer.oid}'])
    )[-1]
  ).register_path(

    'add',
    Node().set_init_func(
      lambda ctx: (
        article := OfferArticle.create(offer=Offer.get(oid=ctx.params['oid'])),
        Redirect.create_go([f'choose?oaid={article.oaid}'])
      )[-1]
    ).register_path(

      'choose',
      ListNode(
        options_gen={
          opt: lambda ctx: (
            (
              article := OfferArticle.get(oaid=ctx.params['oaid']).set('article', ctx.text),
              Redirect.create_move(
                [f'quantity?oaid={article.oaid}']
              )
            )[-1] if opt != texts.participar_o_opts[-1] else Redirect.create_go(['other'])
          ) for opt in texts.participar_o_opts
        },
        init=texts.participar_o,
        back=lambda ctx: Redirect.create_back(2) if not ctx.params['another'] else Redirect.create_move(['final?oid=' + str(ctx.params['oid']), 2])
      ).register_path(

        'other',
        Node().set_init_func(
          lambda ctx: ctx.send_msg(texts.participar_o_otros, reply_markup=teletypes.ReplyKeyboardMarkup(teletypes.KeyboardButton(texts.back)))
        ).set_func(
          lambda ctx: (
            (
              article := OfferArticle.get(oaid=ctx.params['oaid']).set('article', ctx.text),
              Redirect.create_go([f'quantity?oaid={article.oaid}'], 1)
            )[-1] if ctx.text != texts.back else Redirect.create_back()
          )
        )
      )
    ).register_path(

      'quantity',
      FormNode(
        final=lambda ctx: (
          article := OfferArticle.get(oaid=ctx.params['oaid']).set('quantity', ctx.params['answers'][0]),
          Redirect.create_move([f'description?oaid={article.oaid}'])
        )[-1],
        back=lambda ctx: Redirect.create_move(['choose?oaid=' + str(ctx.params['oaid'])])
      ).add_questions(
        (
          texts.participar_o_cantidad,
          lambda ctx: False if ctx.text.isdigit() and int(ctx.text) > 0 else texts.participar_o_cantidad_numero,
          lambda ctx: int(ctx.text)
        )
      )
    ).register_path(

      'description',
      FormNode(
        final=lambda ctx: (
          article := OfferArticle.get(oaid=ctx.params['oaid']).set('description', ctx.params['answers'][0]),
          Redirect.create_move([f'final?oid=' + str(ctx.params['oid'])], 2)
        )[-1],
        back=lambda ctx: Redirect.create_move(['quantity?oaid=' + str(ctx.params['oaid'])])
      ).add_questions(
        (
          texts.participar_o_descripcion,
          lambda ctx: False if len(str(ctx.text)) > 0 else texts.participar_o_descripcion_no
        )
      )
    )
  ).register_path(

    'final',
    Node().set_init_func(
      Redirect.create_go(['more'])
    ).register_path(

      'more',
      BooleanNode(
        init=texts.participar_o_otro,
        true=lambda ctx: Redirect.create_move(['add?another=True&oid=' + str(ctx.params['oid'])], 2),
        false=Redirect.create_move(['who']),
        true_field=texts.participar_o_otro_si,
        false_field=texts.participar_o_otro_no
      )
    ).register_path(
      
      'who',
      FormNode(
        final=lambda ctx: (
          ctx.user.set_temp_name('answers', ctx.params['answers']),
          Redirect.create_move(['part'])
        )
      ).add_questions(
        (
          texts.participar_o_final_quien,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_nombre,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_persona,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_telefono,
          lambda ctx: False if ctx.isdigit() and int(ctx.text) > 0 else texts.invalid_answer
        ),
        (
          texts.participar_o_final_email,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_ciudad,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_cp,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        ),
        (
          texts.participar_o_final_calle,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer
        )
      )
    ).register_path(

      'part',
      BooleanNode(
        init=texts.participar_o_final_unirse,
        true=lambda ctx: (
          ctx.user.append_temp_name('answers', True),
          Redirect.create_move('send')
        )[-1],
        false=lambda ctx: (
          ctx.user.append_temp_name('answers', False),
          Redirect.create_move('send')
        )[-1],
        true_field=texts.participar_o_final_unirse_si,
        false_field=texts.participar_o_final_unirse_no
      )
    ).register_path(

      'send',
      Node().set_init_func(
        lambda ctx: (
          ctx.send_msg(texts.participar_o_enviar, reply_markup=(
            teletypes.ReplyKeyboardMarkup(
              teletypes.KeyboardButton(texts.participar_o_enviar_button)
            )
          ))
        )
      ).set_func(
        lambda ctx: (
          (
            Redirect.create_go([])
          ) if ctx.text != texts.participar_o_enviar_button else (
            ctx.send_msg(texts.participar_o_enviado),
            Redirect.create_to(['']).no_exc()
          )[-1]
        )
      )
    )
  )
)

participar_n_node = None



