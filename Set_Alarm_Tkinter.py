from  tkinter import *
import datetime
import time
import pyttsx3
synthesizer = pyttsx3.init()

window=Tk()
Alarm_time=""
window.config(pady=20)
window.geometry("300x300")
window.title("Alarm")
entry=Entry()
entry.insert(0,"hh:mm:ss")
entry.pack()
label_emtpy=Label(text="")
label_emtpy.pack()
def settime():
    global Alarm_time
    Alarm_time=entry.get()

button=Button(text="Set",command=settime,padx=5)
button.pack()
canvas=Canvas()


def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

create_circle(150, 100, 60, canvas)
current_time=datetime.datetime.now().strftime("%H:%M:%S")

canvas.create_text(150,90,text=f"{current_time}",font=('Arial',10,'bold '))

canvas.pack()

def add_a():
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    canvas.delete('all')
    create_circle(150, 100, 60, canvas)
    canvas.create_text(150,90,text=f"{current_time}",font=('Arial',10,'bold '))
    if(current_time==Alarm_time):
        synthesizer.say("ITS TIME TO LEAVE BED BUDDY"*20)
        synthesizer.runAndWait()
        synthesizer.stop()
        time.sleep(1)

    window.after(1000, add_a)  # <== re-schedule add_a

window.after(1000, add_a)
window.mainloop()