# Python 3.10 09.10.2021


from tkinter import *
import os

ustimed = 0
def get_data():
    ustimed = str(ustime.get())
    stdn = open("shtdwn.bat", "w")
    stdn.write("shutdown -s -t ")
    stdn.write(str(ustimed))
    stdn.close()
    tk.destroy()
    os.system("shtdwn.bat")
    
tk = Tk()
tk.geometry("150x150")
ustime = Entry(tk)
ustime.pack()
but = Button(tk, text = "input sec", command = get_data)
but.pack()
tk.mainloop()





