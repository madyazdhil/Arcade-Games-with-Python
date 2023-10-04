def Vol_tab():
    phi = 3.14
    r = 7
    t = 14
    vt = phi*(r**2)*t
    print(vt)

Vol_tab()

#function with parameter
def Vol_tab1(r, t):
    phi = 3.14
    vt = phi*(r**2)*t
    print(vt)

Vol_tab1(14,7)

#function with return value
def Vol_tab2(r, t):
    phi = 3.14
    vt = phi*(r**2)*t
    return vt

c = Vol_tab2(14,7)
print(c)

sandwich = ["strwb","Turkey","PBJ", "blbry","choco"]
print(sandwich)
print(sandwich[0])
print(sandwich[len(sandwich)-1])


import tkinter as tk
import tkinter.messagebox as mg

win = tk.Tk()
win.geometry("300x300")
win.title("MyButtons")

def showInfo():
    mg.showinfo("Info aja","Kamu klik button saya")

def alert():
    mg.showwarning("WARNING!!!!","Kamu klik button saya")

btn1 = tk.Button(win, text="Button 1", command=alert)
btn2 = tk.Button(win, text="Button 2", command=showInfo)

btn1.pack()
btn2.pack()

win.mainloop()