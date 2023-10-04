def vol_tabung(r,t):
    phi = 3.14
    vol= phi*(r**2)*t

    return vol

vT=vol_tabung(14,7)

print(f"HAsil perhitungan volume Tabung adalah {vT}")

sandwich = ["Strwbry", "Blbry", "Chcklt", "pinaple","","dsds"]
print(sandwich)
print(sandwich[0])
print(sandwich[len(sandwich)-1])


import tkinter as tk
import tkinter.messagebox as mg

window = tk.Tk()
window.geometry("300x300")
window.title("My Button")

def showInfo():
    mg.showinfo("Info","You have clicked a button")
def ShowWarning():
    mg.showwarning("Info","You have clicked a button")

btn1 = tk.Button(window, text="Button1",command=ShowWarning)
btn2 = tk.Button(window, text="Button2",command=showInfo)

btn1.pack()
btn2.pack()

window.mainloop()