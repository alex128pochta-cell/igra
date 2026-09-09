@echo off
chcp 65001 >nul
title Математическая Магия - Установка и Запуск

echo ╔════════════════════════════════════════════════════════╗
echo ║           МАТЕМАТИЧЕСКАЯ МАГИЯ                        ║
echo ║              Добро пожаловать!                        ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo Проверка системы...
echo.

REM Проверка наличия Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] Python не найден на вашем компьютере!
    echo.
    echo Для запуска игры необходимо установить Python:
    echo 1. Перейдите на сайт https://www.python.org/downloads/
    echo 2. Скачайте последнюю версию Python
    echo 3. Запустите установщик
    echo 4. ВАЖНО: Поставьте галочку "Add Python to PATH"
    echo 5. Нажмите "Install Now"
    echo.
    echo После установки Python запустите этот файл снова.
    echo.
    pause
    exit /b 1
)

echo [OK] Python найден!
python --version
echo.

REM Проверка файла игры
if not exist "game.py" (
    echo [ОШИБКА] Файл game.py не найден!
    echo Убедитесь, что вы распаковали все файлы из архива.
    echo.
    pause
    exit /b 1
)

echo [OK] Файлы игры найдены!
echo.
echo ════════════════════════════════════════════════════════
echo Игра готова к запуску!
echo ════════════════════════════════════════════════════════
echo.
echo Запуск игры...
echo.

python game.py

if %errorlevel% neq 0 (
    echo.
    echo [ОШИБКА] Произошла ошибка при запуске игры.
    echo.
    echo Возможные причины:
    echo - Не установлена библиотека tkinter (обычно идёт с Python)
    echo - Проблема с графическим интерфейсом
    echo.
    echo Попробуйте переустановить Python с официального сайта.
    echo.
    pause
    exit /b 1
)

echo.
echo Игра завершена.
pause
