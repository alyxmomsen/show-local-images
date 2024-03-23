import os
import glob
import tkinter as tk
from PIL import Image, ImageTk

# Определите путь к папке с изображениями
image_folder = "путь_к_папке_с_изображениями"

# Создайте список файлов изображений в папке
image_files = glob.glob(os.path.join(image_folder, "*.jpg"))  # Можете изменить расширение файла, если требуется

# Создайте окно
window = tk.Tk()

# Создайте виджет для отображения изображений
image_label = tk.Label(window)
image_label.pack()

# Функция для отображения следующего изображения
def show_next_image():
    # Получите следующий файл изображения
    current_image = image_files.pop(0)
    image_files.append(current_image)
    
    # Откройте изображение с помощью библиотеки PIL
    image = Image.open(current_image)
    
    # Измените размер изображения, если требуется
    # image = image.resize((width, height))
    
    # Создайте объект ImageTk для отображения в окне tkinter
    image_tk = ImageTk.PhotoImage(image)
    
    # Обновите изображение в виджете
    image_label.config(image=image_tk)
    image_label.image = image_tk
    
    # Установите интервал между отображениями изображений (в миллисекундах)
    window.after(2000, show_next_image)  # Можете изменить интервал, если требуется

# Начните отображение изображений
show_next_image()

# Запустите главный цикл окна
window.mainloop()
