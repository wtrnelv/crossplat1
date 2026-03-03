import tkinter as tk

# модель - тільки дані
class daymodel:
    def __init__(self):
        self.days = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]
        self.counter = 0 # внутрішній лічильник

    def step_up(self):
        self.counter = (self.counter + 1) % len(self.days) # збільшую індекс

    def step_down(self):
        self.counter = (self.counter - 1) % len(self.days) # зменшую індекс

    def reset_counter(self):
        self.counter = 0 # скидаю на самий початок

    def get_data(self):
        return self.days[self.counter], self.counter + 1  # повертаю назву дня та індекс


# в'ю - тільки малювання віконець та кнопок
class dayview(tk.Frame):
    def __init__(self, master, callbacks):
        super().__init__(master) # ініціалізую фрейм
        self.pack(pady=20)

        # створюю напис для назви дня
        self.label_day = tk.Label(self, text="", font=("arial", 22, "bold"), width=15)
        self.label_day.pack()

        # створюю напис для відображення порядкового номера
        self.label_idx = tk.Label(self, text="", font=("arial", 12))
        self.label_idx.pack(pady=5)

        # створюю кнопки
        tk.Button(self, text="вперед", command=callbacks['next'], width=15).pack(pady=2)
        tk.Button(self, text="назад", command=callbacks['prev'], width=15).pack(pady=2)
        tk.Button(self, text="скинути", command=callbacks['reset'], width=15).pack(pady=2)

    def update_display(self, day_name, index):
        self.label_day.config(text=day_name) # метод для оновлення тексту на екрані
        self.label_idx.config(text=f"поточний індекс: {index}")


# контролер - зв'язує модель і в'ю
class daycontroller:
    def __init__(self, root):
        self.model = daymodel() # створюю екземпляр моделі
        
        # готую словник функцій
        callbacks = {
            'next': self.handle_next,
            'prev': self.handle_prev,
            'reset': self.handle_reset
        }
        
        # створюю екземпляр в'ю, передаючи їй функції контролера
        self.view = dayview(root, callbacks)
        self.update_view()

    def handle_next(self):
        self.model.step_up() # натиснута кнопка "вперед" -> кажемо моделі змінити дані
        self.update_view()

    def handle_prev(self):
        self.model.step_down() # натиснута кнопка "назад" -> кажемо моделі відняти 1
        self.update_view() 

    def handle_reset(self):
        self.model.reset_counter() # натиснуто "скинути" -> модель ставить 0
        self.update_view()

    def update_view(self):
        day, idx = self.model.get_data() # беру свіжі дані з моделі, передаю їх у в'ю для відмальовки
        self.view.update_display(day, idx)


# головний блок запуску
if __name__ == "__main__":
    root = tk.Tk()
    root.title(" дні тижня")
    root.geometry("600x560")
    
    # ініціалізуємо контролер, який запускає всю логіку
    app = daycontroller(root)
    
    # запускаємо нескінченний цикл обробки подій вікна
    root.mainloop()