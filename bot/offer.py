
from teleframework.shortcuts import *

offer_node = Node()

@offer_node.init_func_decorator()
def _(ctx: BaseContext):
    offer = Offer.create(user=ctx.user)
    ctx.user.set_temp_name('oid', offer.oid)
    return Redirect.create_go([f'add?another=False'])


# Add Node
add_node = Node()

@add_node.init_func_decorator()
def _(ctx: BaseContext):
    article = OfferArticle.create(
        offer=Offer.get(oid=ctx.user.temp_name('oid'))
    )
    return Redirect.create_go([f'choose?oaid={article.oaid}'])

# Choose
add_node.register_path(
    'choose',
    ListNode(
        options_gen=lambda ctx: (
            {
                opt: (
                    lambda ctx: (
                        article := OfferArticle.get(
                            oaid=ctx.params['oaid']
                        ).set(
                            'article',
                            ctx.text
                        ),
                        Redirect.create_move(
                            [f'quantity?oaid={article.oaid}']
                        )
                    )[-1] if not ctx.text == texts.participar_o_opts[-1] else (
                        Redirect.create_go(['other'])
                    )
                ) for opt in texts.participar_o_opts
            }
        ),
        init=lambda ctx: ctx.send_msg(
            texts.participar_o.format(
                num=len(
                    [a for a in Offer.get(oid=ctx.user.temp_name('oid')).articles]
                )
            ),
            default_markup=True
        ),
        back=lambda ctx: (
            (
                Redirect.create_back(3)
            ) if not ctx.params['another'] else (
                Redirect.create_move([
                    'final?oid=' + str(ctx.user.temp_name('oid'))
                ], 2)
            )
        )
    ).register_path(
        'other',
        Node().set_init_func(
          lambda ctx: ctx.send_msg(texts.participar_o_otros, reply_markup=teletypes.ReplyKeyboardMarkup(teletypes.KeyboardButton(texts.back)))
        ).set_func(
          lambda ctx: (
            (
                article := OfferArticle.get(
                    oaid=ctx.params['oaid']
                ).set(
                    'article', ctx.text
                ),
                Redirect.create_move(
                    [f'quantity?oaid={article.oaid}'],
                    2
                )
            )[-1] if ctx.text != texts.back else (
                Redirect.create_back()
            )
          )
        )
    )
)

# Quantity
add_node.register_path(
    'quantity',
    FormNode(
        final=lambda ctx: (
            article := OfferArticle.get(
                oaid=ctx.params['oaid']
            ).set(
                'quantity',
                ctx.params['answers'][0]
            ),
            Redirect.create_move(
                [f'description?oaid={article.oaid}']
            )
        )[-1],
        back=lambda ctx: Redirect.create_move(
            [
                'choose?oaid=' + str(ctx.params['oaid'])
            ]
        )
    ).add_questions(
        (
            texts.participar_o_cantidad,
            lambda ctx: (
                (
                    False
                ) if ctx.text.isdigit() and int(ctx.text) > 0 else (
                    texts.participar_o_cantidad_numero
                )
            ),
            lambda ctx: int(ctx.text)
        )
    )
)

# Description
add_node.register_path(
    'description',
    FormNode(
        final=lambda ctx: (
            article := OfferArticle.get(
                oaid=ctx.params['oaid']
            ).set(
                'description',
                ctx.params['answers'][0]
            ),
            Redirect.create_move(
                ['final?oid=' + str(ctx.user.del_temp_name('oid', get=True))],
                2
            )
        )[-1],
        back=lambda ctx: Redirect.create_move(
            ['quantity?oaid=' + str(ctx.params['oaid'])]
        )
    ).add_questions(
        (
            texts.participar_o_descripcion,
            lambda ctx: False if len(str(ctx.text)) > 0 else texts.participar_o_descripcion_no
        )
    )
)


# Final Node
final_node = Node()

final_node.set_init_func(
    lambda ctx: Redirect.create_go(['more'] if len([a for a in Offer.get(oid=ctx.params['oid']).articles]) < 3 else ['who'])
)

# More
final_node.register_path(
    'more',
    BooleanNode(
        init=texts.participar_o_otro,
        true=lambda ctx: (
            ctx.user.set_temp_name('oid', ctx.params['oid']),
            Redirect.create_move(
                ['add?another=True'],
                2
            )
        )[-1],
        false=Redirect.create_move(['who']),
        true_field=texts.participar_o_otro_si,
        false_field=texts.participar_o_otro_no
    )
)

# Who
final_node.register_path(
    'who',
    FormNode(
        final=lambda ctx: (
          update_offer(ctx.params['answers']),
          Redirect.create_move(['part'])
        )[-1]
    ).add_questions(
        (
          texts.participar_o_final_quien,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('quien', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_nombre,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('nombre', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_persona,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('persona', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_telefono,
          lambda ctx: False if ctx.text.isdigit() and int(ctx.text) > 0 else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('telefono', ctx.text),
              int(ctx.text)
          )[-1]
        ),
        (
          texts.participar_o_final_email,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('email', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_ciudad,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('ciudad', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_cp,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('cp', ctx.text),
              ctx.text
          )[-1]
        ),
        (
          texts.participar_o_final_calle,
          lambda ctx: False if len(str(ctx.text)) else texts.invalid_answer,
          lambda ctx: (
              Offer.get(user=ctx.user, finished=False).set('calle', ctx.text),
              ctx.text
          )[-1]
        )
    )
)

# Part
final_node.register_path(
    'part',
    BooleanNode(
        init=texts.participar_o_final_unirse,
        true=lambda ctx: (
            Offer.get(user=ctx.user, finished=False).set('unirse', True),
            Redirect.create_move(['send'])
        )[-1],
        false=lambda ctx: (
            Offer.get(user=ctx.user, finished=False).set('unirse', False),
            Redirect.create_move(['send'])
        )[-1],
        true_field=texts.participar_o_final_unirse_si,
        false_field=texts.participar_o_final_unirse_no
    )
)

from bot.api import post_offer

# Send
final_node.register_path(
    'send',
    Node().set_init_func(
    lambda ctx: (
        ctx.send_msg(
            texts.participar_o_enviar,
            reply_markup=(
                teletypes.ReplyKeyboardMarkup().row(
                    teletypes.KeyboardButton(texts.participar_o_enviar_button),
                    teletypes.KeyboardButton(texts.participar_buttons_cancelar)
                )
            )
        )
    )
    ).set_func(
        lambda ctx: (

            (
                Redirect.create_go(['']) if ctx.text == texts.participar_buttons_cancelar else Redirect.create_go([])
            ) if ctx.text != texts.participar_o_enviar_button else (
                post_offer(Offer.get(user=ctx.user, finished=False).toggle('finished')),
                ctx.send_msg(texts.participar_o_enviado),
                Redirect.create_to([''])
            )[-1]
        )
    )
)


offer_node.register_path(
    'add',
    add_node
).register_path(
    'final',
    final_node
)


def setup(node: Node):

    node.register_path(
        'offer',
        offer_node
    )

