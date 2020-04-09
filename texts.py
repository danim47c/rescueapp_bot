
#TODO Config Texts

#? Logging messages

logging_configure = 'Bot initializing'

logging_start = 'Bot started successfully [{seconds} seconds initializing]'

logging_stop = 'Bot stopped successfully [{hours} hours running]'

logging_critical_error = 'Critical error while running bot'

logging_command_not_found = 'I couldn\'t find "{command}" executed by @{user}(ID:{user_id})'

logging_unreachable_path = '@{user}(ID:{user_id}) was in an unreachable path [Path: {path} | Point: \'{point}\']'
logging_unreachable_path_redirected = '@{user}(ID:{user_id}) was redirected to an unreachable path [Path: {path} | Point: \'{point}\']'

logging_no_setup_function = 'All modules need a setup function [Module: {module}]'

logging_questionid_not_found = 'I could\'t find {qid} in {path} '

#? Buttons

back = 'Atras'

done = 'Hecho'

okay = 'Vale'

true_field = 'Verdadero'
false_field = 'Fakse'

# Both strings need the same length
emoji_yes = ' - ✅'
emoji_no = ' - ❌'

#? Default Checks

answer_no_more = 'The answer can\'t contain more than {num} characters'
answer_no_less = 'The answer can\'t contain less than {num} characters'

answer_must_text = 'The answer must contain a text'
answer_must_image = 'The answer must be a photo and that\'s not'
answer_must_int = 'The answer must be a integer'
answer_must_int_between = 'The answer must be a integer between {min} and {max}'

answer_gt = 'The answer must be greater than {num}'
answer_lt = 'The answer must be lower than {num}'


#TODO Custom Texts


info_1 = 'Centralización y emparejamiento de la oferta y la demanda de recursos sanitarios para la lucha contra el COVID-19'

info_2 = 'Nuestra misión principal es atender la creciente necesidad de recursos sanitarios. Lo hacemos mediante la centralización de la oferta y la demanda y así hacer el emparejamiento más óptimo.'

info_2_img = 'AgACAgQAAxkBAAMNXo2IwAmunhs2F7YWOjDSITisJiQAAoeyMRvuoWlQ4nUx8oZALN-T1pgiXQADAQADAgADbQADHu4BAAEYBA'

info_3 = '''Ayúdanos a ayudar a todos

    ✅  Productos
            Te ayudamos a donar o a solicitar gafas, mascarillas, alimentos y mucho más.

    ✅  Material
            Cubrir las necesidades de material para elaborar los productos y utensilios, sobretodo textil impermeable y PVC.

    ✅  Maquinaria
            ¿Tienes o necesitas un taller de costura, impresoras 3D u otras herramientas?
'''

info_4 = '''Nuestros valores

  Coordinación y acción conjunta
  
    Solidaridad
        Apoyo incondicional a la causa en los momentos dificiles.

    Impacto
        Efecto intenso en la vida de la gente que lo necesita.

    Eficacia
        Capacidad para producir resultados.

    Trabajo en equipo
        Diversidad con un mismo objetivo.  
  
'''

participar = '¿Ofreces o necesitas algo?'

participar_buttons_o = 'Ofrezco'
participar_buttons_n = 'Necesito'
participar_buttons_cancelar = 'Cancelar'

participar_o = 'Elige lo que ofreces #{num}'
participar_o_otros = '¿Que es específicamente?'
participar_o_opts = [
  'Alimentación',
  'Batas',
  'Donaciones económicas (€)',
  'Gafas',
  'Gel desinfectante',
  'Guantes',
  'Mascarillas',
  'Materiales (textil, pvc...)',
  'Mensajería',
  'Pantallas faciales',
  'Respiradores',
  'Otros'
]
participar_o_cantidad = '¿Qué cantidad ofreces?'
participar_o_cantidad_numero = 'La cantidad debe ser un número'

