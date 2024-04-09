## Русскоязычный бот на базе ЧатГПТ, кого зовут 'Юрий'
import speech_recognition as sr
import os
from gtts import gTTS
from io import BytesIO
from dotenv import load_dotenv
import openai

load_dotenv()
openai.YURIS_KEY = os.getenv('OPENAI_SECRET')

# Отпределите функции, которые слушает пользователя, общается моделю ЧатГПТ, и говорит пользователю
r = sr.Recognizer()

def Speak(body):
    mp3_fp = BytesIO()
    spoken = gTTS(body, lang='ru')
    spoken.write_to_fp(mp3_fp)
    return mp3_fp

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                
        except sr.RequestError as e:
            print('Could not request results; {0}'.format(e))
        except sr.UnknownValueError:
            print('Unknown Error Occurred')

def send_to_chatGPT(messages, model='gpt-3.5-turbo'):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = []
while(1):
    text = sr.record_text()
# ЧатГПТ понимает сообщения как словарь роли, содержания
    messages.append({'role': 'user', 'content': text})
    response = send_to_chatGPT(messages)
# Юрий произносит сообщение пользователю
    Speak(response)
    
    print(response)
