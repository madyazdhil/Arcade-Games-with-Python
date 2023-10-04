import tkinter as tk
from tkinter import messagebox

class ButtonWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Example")
        self.root.geometry("300x300")

        # Create the buttons
        self.button1 = tk.Button(root, text="Button 1",font=("Arial",20),pady=10, padx=14, command=self.show_info)
        self.button2 = tk.Button(root, text="Button 2",font=("Arial",20),pady=10, padx=14, command=self.show_warning)

        # Pack the buttons into the window
        self.button1.pack(pady=20)
        self.button2.pack()

    def show_info(self):
        messagebox.showinfo("Info", "You have clicked Button 1!")

    def show_warning(self):
        messagebox.showwarning("Warning", "You have clicked Button 2!")


root = tk.Tk()
ButtonWindow(root)
root.mainloop()
