## ----------------Русскоязычный бот на базе ЧатГПТ, кого зовут 'Юрий' ----------------##
import speech_recognition as sr
import os
from gtts import gTTS
from io import BytesIO
from dotenv import load_dotenv
import openai
import tkinter as tk

load_dotenv()

openai.YURIS_KEY = os.getenv('OPENAI_SECRET')
r = sr.Recognizer()

# Отпределите функции, которые слушает пользователя, общается моделю ЧатГПТ, и говорит пользователю
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

def main_loop():
    messages = []
    while(1):
        text = sr.record_text()
# ЧатГПТ понимает сообщения как словарь роли, содержания
        messages.append({'role': 'user', 'content': text})
        response = send_to_chatGPT(messages)
# Юрий произносит сообщение пользователю
        Speak(response)
    
        reponse_text = response.text


##---------------- Графический Ползователья Интерфейс Юрия ----------------##
window = tk.Tk()
window.title('Юрий Компьютеров- Роботизированний партнер дла разговорнoго реча по-русски')
window.geometry('750x500')
window.after_idle(main_loop)
canvas = tk.Canvas()
yuri_image = tk.PhotoImage(file='assets/юрий_фото.png')
window.mainloop()