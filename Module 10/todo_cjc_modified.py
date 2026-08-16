"""
CSD-325 - Module 10
Christopher Craig
Scrolling To-Do App - Modified Version

Base code: Listing 2.2 "Our Scrolling To-Do" (Love, D. Python Tkinter By Example)

Modifications made to the base listing:
    1. Window title changed to "Craig-ToDo"
    2. Added a File menu (steel blue / orange - complementary colours) with an
       Exit option that closes the program
    3. Tasks are now deleted with a RIGHT mouse click instead of a left click
    4. The header label now tells the user how to delete a task
"""

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # --- Modification 1: window title changed to last name-ToDo ---
        self.title("Craig-ToDo")
        self.geometry("300x400")

        # --- Modification 2: File menu with complementary colours and an Exit option ---
        self.menu_bar = tk.Menu(self, bg="steelblue", fg="orange")

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="steelblue", fg="orange")
        self.file_menu.add_command(label="Exit", command=self.exit_program)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.config(menu=self.menu_bar)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # --- Modification 4: header label now includes delete instructions ---
        todo1 = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here ---\nRight-click a task to delete it",
            bg="lightgrey", fg="black", pady=10,
            wraplength=280, justify="center"
        )

        # --- Modification 3: right mouse click (Button-3) deletes a task ---
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            # --- Modification 3: right mouse click (Button-3) deletes a task ---
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

    # --- Modification 2: File -> Exit closes the program correctly ---
    def exit_program(self):
        self.destroy()

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
