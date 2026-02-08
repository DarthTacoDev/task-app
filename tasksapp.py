import customtkinter as ct
import time
from pathlib import Path

# creates a new task
def button_event():
    new_task = TaskRow(app)
    new_task.pack(padx=20, pady=10, fill="x")
    app.tasks.append(new_task) # add new task to list
    new_task.entry.focus()

def load_data():
    if Path("data.txt").exists():
        with open('data.txt', 'r') as file:
            for line in file:
                clean_text = line.strip() # gets the raw string
                
                # make sure line exists
                if clean_text:
                    saved_task = TaskRow(app, clean_text)
                    saved_task.pack(padx=20,pady=10,fill='x')
                    app.tasks.append(saved_task)

# modular task row system
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
        self.save_to_file()
    
    def add_new_task(self):
        new_task = TaskRow(self)
        new_task.pack(padx=20, pady=10, fill="x")
        new_task.entry.focus()

    def get_text(self):
        return self.entry.get()

    def annihilate(self):
        if self in app.tasks:
            app.tasks.remove(self)

        self.destroy()
        app.after(100, self.save_to_file)

    def is_checked(self):
        # check if the task is currently checked
        if self.checkbox.get() == 1:

            self.font.configure(overstrike=True)
            self.entry.configure(text_color="gray")

            # reschedules annihilation after x amount of miliseconds (1000ms = 1s)
            self.after(200, self.annihilate)
    
    def save_to_file(self):
        with open('data.txt', 'w') as file:
            for task in app.tasks:
                text = task.get_text()
                file.write(f"{text}\n")
            print("All tasks added to data.txt")


# App setup/loop
ct.set_default_color_theme("dark-blue") # Themes: dark-blue, green, blue (standard)
ct.set_appearance_mode("system") # system, light, dark

app = ct.CTk()
app.geometry("500x400")
app.title("Tasks")
app.tasks = []

add_task_button = ct.CTkButton(app, text="Add a task", command=button_event)
add_task_button.pack(padx=10, pady=10, fill="x")

# row1 = TaskRow(app, "Buy Milk")
# row1.pack(padx=20, pady=10, fill="x")

# row2 = TaskRow(app, "Finish Python Project")
# row2.pack(padx=20, pady=10, fill="x")

load_data()
app.mainloop()