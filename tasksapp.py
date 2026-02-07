# ctrl + / = comment out

import customtkinter as ct
import time

# creates a new task
def button_event():
    new_task = TaskRow(app)
    new_task.pack(padx=20, pady=10, fill="x")
    new_task.entry.focus()

class TaskRow(ct.CTkFrame):
    def __init__(self, master, task_text="New Task"):
        super().__init__(master, fg_color="transparent")

        # checkbox
        self.checkbox = ct.CTkCheckBox(self, text="", command=self.is_checked)
        self.checkbox.pack(side="left", padx=(0,5))

        # entry
        self.font = ct.CTkFont(family="Segoe UI", size=13)
        self.entry = ct.CTkEntry(self, font=self.font, placeholder_text=task_text, fg_color="transparent", border_width=0, width=0)
        self.entry.insert(0, task_text)
        self.entry.pack(side="left", fill="x", expand=True)

        # save text
        self.entry.bind("<Return>", self.save_task)
    
    def save_task(self, event=None):
        print(f"Task updated to: {self.entry.get()}")
        self.focus() # removes focus from entry
    
    def add_new_task(self):
        new_task = TaskRow(self)
        new_task.pack(padx=20, pady=10, fill="x")
        new_task.entry.focus()

    def annihilate(self):
        self.destroy()

    def is_checked(self):
        # check if the task is currently checked
        if self.checkbox.get() == 1:

            self.font.configure(overstrike=True)
            self.entry.configure(text_color="gray")

            # reschedules annihilation after x amount of miliseconds (1000ms = 1s)
            self.after(200, self.annihilate)
            

# App setup/loop
ct.set_default_color_theme("dark-blue") # Themes: dark-blue, green, blue (standard)
ct.set_appearance_mode("system") # system, light, dark

app = ct.CTk()
app.geometry("500x400")
app.title("Tasks")

add_task_button = ct.CTkButton(app, text="Add a task", command=button_event)
add_task_button.pack(padx=10, pady=10, fill="x")

# row1 = TaskRow(app, "Buy Milk")
# row1.pack(padx=20, pady=10, fill="x")

# row2 = TaskRow(app, "Finish Python Project")
# row2.pack(padx=20, pady=10, fill="x")

app.mainloop()