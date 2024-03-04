import tkinter as tk #tkinter as tk - імпортує бібліотеку для створення графічного інтерфейсу та надає їй ім'я tk
from tkinter import ttk #імпортує частину бібліотеки tkinter, яка містить розширені елементи інтерфейсу
from datetime import datetime # імпортує клас datetime з модуля datetime, щоб працювати з об'єктами дати та часу

def get_selected_datetime(): #оголошення функції  яка отримує значення дати та часу введені користувачем і виводить ці значення в консоль
    year = int(year_spin.get()) #отримання року з елементу year_spin (спінбокс для вибору року) та перетворення його на ціле число
    month = int(month_spin.get()) #Аналогічно для month, day, hour, та minute, вони отримують значення з спінбоксів
    day = int(day_spin.get())
    hour = int(hour_spin.get())
    minute = int(minute_spin.get())
    selected_datetime = datetime(year, month, day, hour, minute) #приймання значень
    # Отримання дня тижня за допомогою strftime
    day_of_week = selected_datetime.strftime("%A") #.strftime("%A") - метод форматує дату у рядок за шаблоном "%A",% формато для отримання назви дня тижня.
    # Він використовується для вичі саме назву дня тижня обраної дати.
    print("Selected Date and Time:", selected_datetime) #виводить обрану дату та час у форматі datetime
    print("Day of the Week:", day_of_week) #виводить назву дня тижня, яку отримали за допомогою методу strftime(), у вигляді рядка.


root = tk.Tk() #створення вікна програми
root.title("Date and Time Picker") #встановлення заголовку для вікна

# Вибір дати
date_frame = ttk.Frame(root) # створення рамки (контейнера) для вибору дати
date_frame.pack(padx=10, pady=10) #розміщення рамки у вікні з відступами 10 пікселів зліва та зверху

ttk.Label(date_frame, text="Year:").grid(row=0, column=0) #створення надпису "Year:" для вибору року
#date_frame контейнер, у якому розміщуемо текстовий елемент
#grid(row=0, column=0) розміщення напису у вікні за координатами row=0 перший рядок та column=0 перший стовпець
year_spin = ttk.Spinbox(date_frame, from_=2000, to=2100, width=5) #from_=2000, to=2100 межі для вибору значень року від 2000 до 2100.width=5 - ширина спінбоксу на 5 символів.
year_spin.grid(row=0, column=1, padx=5)#розміщення спінбоксу для вибору дати на першому рядку, другий стовп з відступом 5 пікселів
# Аналогічні дії для елементів вибору місяця, дня, години та хвилини
ttk.Label(date_frame, text="Month:").grid(row=0, column=2)
month_spin = ttk.Spinbox(date_frame, from_=1, to=12, width=3)
month_spin.grid(row=0, column=3, padx=5)

ttk.Label(date_frame, text="Day:").grid(row=0, column=4)
day_spin = ttk.Spinbox(date_frame, from_=1, to=31, width=3)
day_spin.grid(row=0, column=5, padx=5)

# Вибір часу
time_frame = ttk.Frame(root)
time_frame.pack(padx=10, pady=(0, 10))

ttk.Label(time_frame, text="Hour:").grid(row=0, column=0)
hour_spin = ttk.Spinbox(time_frame, from_=0, to=23, width=3)
hour_spin.grid(row=0, column=1, padx=5)

ttk.Label(time_frame, text="Minute:").grid(row=0, column=2)
minute_spin = ttk.Spinbox(time_frame, from_=0, to=59, width=3)
minute_spin.grid(row=0, column=3, padx=5)

get_button = ttk.Button(root, text="Get Date and Time", command=get_selected_datetime) # Створення кнопки
get_button.pack(padx=10, pady=(0, 10)) # Розміщення кнопки у вікні з відступами

root.mainloop() # Запуск головного циклу подій для відображення вікна та обробки подій користувача

