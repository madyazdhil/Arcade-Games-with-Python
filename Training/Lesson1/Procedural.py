import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("300x300")

# Function to display the message box
def show_message():
    messagebox.showinfo("Info", "You have clicked me!")

# Create the buttons
button1 = tk.Button(root, text="Button 1", command=show_message, font=("Arial",20),pady=10, padx=14)
button2 = tk.Button(root, text="Button 2", command=show_message, font=("Arial",20),pady=10, padx=14)

# Pack the buttons into the window
button1.pack(pady=20)
button2.pack()

# Start the Tkinter main loop
root.mainloop()
