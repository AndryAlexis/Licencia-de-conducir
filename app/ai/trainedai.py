from app.ai.openai import ChatGPT
import json

class DriversExamination(ChatGPT):
    """
    Clase para generar preguntas y respuestas de tipo test, modificando las originales para evitar la memorización directa por parte de los alumnos.
    """

    _JSON_TO_RETURN = """
        {
            "question":"AQUÍ LA PREGUNTA",
            "answers":[
                {"text":"AQUÍ UNA RESPUESTA","isCorrect":"AQUÍ SI ES CORRECTA O NO EN BOOLEAN"},
                ...Otras 3 respuestas más
            ]
        }
    """

    _ORDERS_TO_AI = f"""
        Reglas para generación de preguntas y respuestas:

        Preguntas:
            - No deben ser idénticas ni muy similares a las originales.
            - Conservar el significado original.
            - Pueden estar en primera, segunda o tercera persona.
            - No necesitan ser en formato de pregunta.
            - Variar en longitud respecto a la original.

        Respuestas:
            - Similar a las reglas de las preguntas.
            - Basadas en respuestas cortas y largas.
            - Generar 3 respuestas incorrectas basadas en la correcta.
            - La respuesta correcta no debe ser igual a la original.
            - Variar en longitud (corta, mediana, larga).
            - Incluir al menos 2 variaciones de longitud en todas las respuestas.

        Formato de respuesta: 
            - JSON: {_JSON_TO_RETURN}
    """

    def __init__(self, api_key):
        """
        Inicializa la clase DriversExamination.

        Args:
            api_key: Clave de la API de OpenAI.
        """
        super().__init__(api_key)

    def send_message(self, question : str, short_answer : str, long_answer : str) -> json:
        """
        Envía un mensaje a ChatGPT con las órdenes y obtiene la respuesta en formato JSON.

        Args:
            question: La pregunta original.
            short_answer: La respuesta corta original.
            long_answer: La respuesta larga original.

        Returns:
            dict: La respuesta de ChatGPT en formato JSON.
        """
        message = self._orders_to_ai(question=question, 
                                     short_answer=short_answer, 
                                     long_answer=long_answer)
        
        response = super().send_message(message=message)
        dict_response = None

        try:
            dict_response = json.loads(response)
        except Exception as e:
            print('ERROR: ', e)
        finally:
            return dict_response
    
    def _orders_to_ai(self, question : str, short_answer : str, long_answer : str) -> str:
        """
        Genera un mensaje con las órdenes y las respuestas originales.

        Args:
            question: La pregunta original.
            short_answer: La respuesta corta original.
            long_answer: La respuesta larga original.

        Returns:
            str: El mensaje completo con las órdenes y respuestas.
        """
        return f"""
            PREGUNTA: {question} 
            RESPUESTA CORTA: {short_answer}
            RESPUESTA LARGA: {long_answer}

            {self._ORDERS_TO_AI} 
        """
