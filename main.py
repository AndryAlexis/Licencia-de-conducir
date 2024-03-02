from openai import OpenAI
client = OpenAI(api_key='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')
 
try:
    question = 'Si una intersección tiene una señal de pare y un cruce peatonal pero no tiene una línea de pare, ¿usted dónde debe detenerse?.'
    short_answer= 'Antes del cruce peatonal.'
    long_answer = 'En una señal de alto, usted debe detenerse antes de la línea de parada, si hay una. Si no hay línea de parada, debe detenerse antes de ingresar al paso de peatones. Si no hay línea de parada, debe detenerse antes de ingresar al paso de peatones. Si no hay ni una línea de parada ni un paso de peatones, debe detenerse antes de ingresar a la intersección.'

    format = '{"question":"AQUÍ LA PREGUNTA","answers":[{"text":"AQUÍ UNA RESPUESTA","isCorrect":"AQUÍ SI ES CORRECTA O NO EN BOOLEAN"} ...Otras 3 respuestas más]}'

    message = f"""
        PREGUNTA: {question} 
        RESPUESTA CORTA: {short_answer}
        RESPUESTA LARGA: {long_answer}

        La pregunta y las respuestas las replanteas de diversas formas que sea diferente pero sin llegar a perder su significado. Las preguntas y respuestas pueden ser en primera, segundo o tercera persona. La respuesta serán basadas en los 2 tipos de respuesta Tanto la pregunta como las respuestas deben variar en sus longitudes, sobre todo las respuestas. Crea 3 respuestas incorrectas basándote en la correcta. Todo formato json así: {format}
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print('HE PETAO: ', e)
