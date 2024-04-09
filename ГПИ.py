## Графический Пользовательский Интерфейс Юрия Компьютерова
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Юрий Компьютеров')
window.geometry('750x750')
BACKGROUND = tk.PhotoImage(file = 'assets/russian_flag')
background_canvas = tk.Canvas(window, width=500, height=500)
background_canvas.pack(fill ='both', expand=True)
background_canvas.create_image(0, 0, image=BACKGROUND, anchor='nw')

window.mainloop()