# -*- coding: utf-8 -*-
import pyautogui
import time
import keyboard
import os
import pytz
from datetime import datetime
import requests
import sys
import ctypes
import subprocess
os.system(f"title STAL:TRACKER • Загрузка..")

time.sleep(3)
# Проверяем, запущен ли скрипт с правами администратора
# ------------------------
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
#-------------------------------------
# Перезапускаем скрипт с правами администратора, если необходимо
#---------------------------------
if not is_admin():
    # Перезапускаем скрипт с флагом, указывающим, что нужны права администратора
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    # Выходим из текущего процесса
    sys.exit()

# Здесь ваш код, который будет выполнен с правами администратора
print("")
print("Скрипт запущен с правами администратора. GoodLuck!")
print("")
time.sleep(1)
os.system("cls")
time.sleep(0.1)

APP_VERSION = "0.0.4"
UPDATE_URL = "https://github.com/Vu4eke/staltracker-api/raw/main/version.txt" # Version.txt
UPDATE_FILE_URL = "https://github.com/Vu4eke/staltracker-api/raw/main/STALTRACKER%20(ChatBypass).exe" # ChatBypass file
UPDATE_FILE_PATH = "models/STALTRACKER (ChatBypass).exe"


def check_for_update():
    try:
        response = requests.get(UPDATE_URL)
        latest_version = response.text.strip()
        if latest_version != APP_VERSION:
            print("Доступно обновление! Новая версия:", latest_version)
            print("\033[92m>\033[0m Установка...")
            time.sleep(2)
            return True
        else:
            print("У вас установлена последняя версия приложения!")
            return False
    except requests.RequestException as e:
        print("Ошибка при проверке обновлений:", e)
        return False


def download_update():
    try:
        response = requests.get(UPDATE_FILE_URL)
        with open(UPDATE_FILE_PATH, 'wb') as file:
           file.write(response.content)
           print("Обновление загружено успешно:", UPDATE_FILE_PATH)
           time.sleep(5)
    except requests.RequestException as e:
        print("Ошибка при загрузке обновления:", e)
        time.sleep(5)
        subprocess.Popen([UPDATE_FILE_PATH])

if check_for_update():
    download_update()

    

time.sleep(0.6)
os.system("cls")
time.sleep(0.1)

os.system(f"title STAL:TRACKER • Версия: {APP_VERSION}")

print(f"")
print(f"╔ -     \033[92m>\033[0m ChatBypass {APP_VERSION} загружен.       - ╗")
print(f"║ - https://github.com/Vu4eke/staltracker  - ║")
print(f"╚ - Гайд есть на github, посмотри там.     - ╝")
print(f"")


while True:

    text_input = input("Спам-текст: ")

    if text_input.strip():  
        if len(text_input) > 150:
            print("Текст превышает лимит скрипта. Будет использована только часть текста. (150 символов)")
            text_input = text_input[:150]
        break  # Выход из цикла при вводе текста
    else:
        print("Вы не ввели текст. Пожалуйста, введите хотя бы один символ.")



time.sleep(0.1)
print("\n[ - Зайдите в игру, даю вам 5 секунд - ]\n")
time.sleep(5) # - Чтобы пользователь успел перейти в окно.

moscow_tz = pytz.timezone('Europe/Moscow')
time_now = datetime.now(moscow_tz)

time_now_str = time_now.strftime('%H:%M:%S')

os.system("cls")
print(f"")
print(f"╔ -     \033[92m>\033[0m ChatBypass {APP_VERSION} загружен.       - ╗")
print(f"║ - https://github.com/Vu4eke/staltracker  - ║")
print(f"╚ -  Гайд есть на github, посмотри там.    - ╝")
print(f"")
print(f"Лог:")
count = 0
    
while count < 300000000000:
    count += 1
    print(f"\033[90m{time_now_str}\033[0m ChatBypass: {count} отправлено")

    time.sleep(0.1) # ---------------- 1 спам
    keyboard.press("j")
    time.sleep(0.1)
    keyboard.release("j")
    time.sleep(0.1)
    keyboard.write(text_input + "§")  # Добавляем символ "." в конце текста
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1) # ---------------- 2 спам
    keyboard.press("j")
    time.sleep(0.1)
    keyboard.release("j")
    time.sleep(0.1)
    keyboard.write(text_input + "§§")  # Добавляем символ ".." в конце текста
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1) # ---------------- 3 спам
    keyboard.press("j")
    time.sleep(0.1)
    keyboard.release("j")
    time.sleep(0.1)
    keyboard.write(text_input + "§§§")  # Добавляем символ "..." в конце текста
    time.sleep(0.1)
    pyautogui.press("enter")
        
    time.sleep(30)
