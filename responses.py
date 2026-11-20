
import re

def process_message(message, response_array, response):
    # Dividir el mensaje en palabras
    list_message = re.findall(r"[\w']+", message.lower())

    # Contar coincidencias
    score = sum(1 for word in list_message if word in response_array)

    return [score, response]


def get_response(message):
    # Respuestas relacionadas con FitControl
    response_list = [
        process_message(message,
        ['hola', 'holis', 'buenas', 'buenos', 'dias', 'tardes'],
        '¡Hola! Bienvenido a FitControl. ¿En qué puedo ayudarte?'),

        process_message(message,
        ['chau', 'adios', 'hasta', 'luego', 'bye'],
        '¡Hasta luego! Gracias por utilizar FitControl.'),

        process_message(message,
        ['ayuda', 'ayudar', 'problema', 'help'],
        '¡Claro! Puedo ayudarte con tus comidas, actividad física y objetivos.'),

        process_message(message,
        ['comida', 'comidas', 'alimentacion', 'alimento'],
        'En FitControl podes registrar tus comidas y consultar tu alimentación.'),

        process_message(message,
        ['ejercicio', 'actividad', 'fisica', 'entrenamiento'],
        'Podes registrar tus actividades físicas y consultar tu progreso.'),

        process_message(message,
        ['peso', 'pesar', 'kilos'],
        'En FitControl podes registrar tu peso actual y realizar un seguimiento.'),

        process_message(message,
        ['objetivo', 'meta', 'metas'],
        '¡Establecé tus objetivos y seguí tu progreso con FitControl!'),

        process_message(message,
        ['progreso', 'avance', 'estadisticas'],
        'Podes consultar tus registros para conocer tu progreso.'),

        process_message(message,
        ['gracias', 'agradezco'],
        '¡De nada! FitControl está para ayudarte.'),

        process_message(message,
        ['nombre', 'quien', 'sos'],
        'Soy FitControl Bot, tu asistente virtual de hábitos saludables.')
    ]

    # Buscar la respuesta con mayor coincidencia
    response_scores = [response[0] for response in response_list]

    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    if winning_response == 0:
        bot_response = 'No entendí tu mensaje. Podes preguntarme sobre comidas, ejercicio, peso u objetivos.'
    else:
        bot_response = matching_response[1]

    print('Respuesta del Bot:', bot_response)
    return bot_response


# Pruebas del sistema
get_response('Hola, quiero registrar mi peso')
get_response('Como puedo registrar mi actividad fisica?')
get_response('Quiero consultar mis objetivos')
