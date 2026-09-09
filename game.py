import tkinter as tk
from tkinter import font as tkfont


class MathMagicGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Математическая Магия")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Настройка цветов
        self.colors = {
            'bg': '#1a1a2e',
            'fg': '#eee',
            'accent': '#e94560',
            'button_bg': '#16213e',
            'button_hover': '#0f3460'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Создание шрифтов
        self.title_font = tkfont.Font(family="Arial", size=48, weight="bold")
        self.menu_font = tkfont.Font(family="Arial", size=24)
        self.subtitle_font = tkfont.Font(family="Arial", size=16)
        
        self.show_main_menu()
    
    def show_main_menu(self):
        """Отображение главного меню"""
        self.clear_screen()
        
        # Заголовок
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(pady=(80, 0))
        
        title_label = tk.Label(
            title_frame,
            text="✨ Математическая Магия ✨",
            font=self.title_font,
            fg=self.colors['accent'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Почувствуй силу чисел!",
            font=self.subtitle_font,
            fg=self.colors['fg'],
            bg=self.colors['bg']
        )
        subtitle_label.pack(pady=(10, 0))
        
        # Меню кнопок
        menu_frame = tk.Frame(self.root, bg=self.colors['bg'])
        menu_frame.pack(pady=60)
        
        buttons = [
            ("🎮 Начать игру", self.start_game),
            ("📖 Как играть", self.show_instructions),
            ("🏆 Рекорды", self.show_records),
            ("⚙️ Настройки", self.show_settings),
            ("🚪 Выход", self.exit_game)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = self.create_menu_button(menu_frame, text, command)
            btn.pack(pady=10, ipadx=40, ipady=10)
    
    def create_menu_button(self, parent, text, command):
        """Создание кнопки меню с эффектами"""
        btn = tk.Button(
            parent,
            text=text,
            font=self.menu_font,
            fg=self.colors['fg'],
            bg=self.colors['button_bg'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['fg'],
            relief=tk.FLAT,
            cursor="hand2",
            command=command
        )
        
        # Эффект при наведении
        btn.bind("<Enter>", lambda e: e.widget.config(bg=self.colors['button_hover']))
        btn.bind("<Leave>", lambda e: e.widget.config(bg=self.colors['button_bg']))
        
        return btn
    
    def start_game(self):
        """Запуск игры (заглушка)"""
        self.show_message("🎮 Игра скоро начнётся!\n\nЭто демо-версия главного меню.")
    
    def show_instructions(self):
        """Показать инструкцию"""
        self.show_message(
            "📖 Как играть:\n\n"
            "1. Решайте математические примеры\n"
            "2. Зарабатывайте очки за правильные ответы\n"
            "3. Открывайте новые уровни сложности\n"
            "4. Ставьте личные рекорды!\n\n"
            "Удачи в игре!"
        )
    
    def show_records(self):
        """Показать рекорды"""
        self.show_message(
            "🏆 Рекорды:\n\n"
            "Пока нет сохранённых рекордов.\n"
            "Начните играть, чтобы установить свой первый рекорд!"
        )
    
    def show_settings(self):
        """Показать настройки"""
        self.show_message(
            "⚙️ Настройки:\n\n"
            "Настройки будут доступны в полной версии.\n\n"
            "Планируется:\n"
            "- Выбор сложности\n"
            "- Настройка звука\n"
            "- Выбор темы оформления"
        )
    
    def exit_game(self):
        """Выход из игры"""
        self.root.quit()
    
    def show_message(self, message):
        """Показать сообщение в модальном окне"""
        modal = tk.Toplevel(self.root)
        modal.title("Информация")
        modal.geometry("500x400")
        modal.resizable(False, False)
        modal.configure(bg=self.colors['bg'])
        
        # Делаем модальным
        modal.transient(self.root)
        modal.grab_set()
        
        # Центрирование окна
        modal.update_idletasks()
        x = (modal.winfo_screenwidth() - 500) // 2
        y = (modal.winfo_screenheight() - 400) // 2
        modal.geometry(f"500x400+{x}+{y}")
        
        message_label = tk.Label(
            modal,
            text=message,
            font=tkfont.Font(family="Arial", size=14),
            fg=self.colors['fg'],
            bg=self.colors['bg'],
            justify=tk.CENTER
        )
        message_label.pack(expand=True, pady=40)
        
        close_btn = tk.Button(
            modal,
            text="Закрыть",
            font=tkfont.Font(family="Arial", size=16),
            fg=self.colors['fg'],
            bg=self.colors['accent'],
            relief=tk.FLAT,
            cursor="hand2",
            command=modal.destroy
        )
        close_btn.pack(pady=20, ipadx=30, ipady=8)
        
        # Эффект при наведении
        close_btn.bind("<Enter>", lambda e: e.widget.config(bg='#c73e54'))
        close_btn.bind("<Leave>", lambda e: e.widget.config(bg=self.colors['accent']))
    
    def clear_screen(self):
        """Очистка экрана"""
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    game = MathMagicGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
