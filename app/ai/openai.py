
from openai import OpenAI

class ChatGPT:

    _MODEL = 'gpt-3.5-turbo' #Modelo de la IA gratuito
    _ERROR = 'Error en la IA:'
    _KEY_CONTENT_MESSAGE = 'content'
    _MESSAGE = {
        'role' : 'user', #Se expresa a la IA el rol de la persona que le envía el mensaje
        _KEY_CONTENT_MESSAGE : '' #El mensaje que recibirá la IA.
    }

    def __init__(self, api_key : str):
        """
        Inicializa la clase ChatGPT con la clave de la API.

        Args:
            api_key: La clave de la API de OpenAI.
        """

        self._api_key = api_key
        self._client = OpenAI(api_key=self._api_key)
    
    def send_message(self, message : str) -> str:
        """
        Envía un mensaje de texto a chat-gpt y devuelve la respuesta.

        Args:
            message: El mensaje que se enviará a la IA.

        Returns:
            str: La respuesta de la IA al mensaje.
        """

        response = None
        try:
            #Se rellena la el valor de la llave vacía con el mensaje
            self._MESSAGE[self._KEY_CONTENT_MESSAGE] = message

            #Se crea el mensaje que se enviará
            completion = self._client.chat.completions.create(
                model=self._MODEL, #Modelo de la IA que se usará para enviar el mensaje
                messages=[self._MESSAGE] #El mensaje en cuestión
            )
            #Se recoje solo el contenido del mensaje
            response = completion.choices[0].message.content 
        except Exception as e:
            print(self._ERROR, e)
        finally:
            return response
