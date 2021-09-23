from tkinter import *
from datetime import *
from PIL import Image,ImageTk
from ApnaDhaba import *
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
today = date.today()
root=Tk()
root.geometry("600x788")
root.title('Weather Report')
root.iconbitmap('weather.ico')
TitleLabel=Label(text="Weather Report-Kolkata",font=("Arial Bold", 25))
DateLabel=Label(text=f"{today}",font=("Arial Bold", 15))
TextLabel=Label(text="Today's temperature in Kolkata is 28°c. Day's maximum temperature would hover at 37°c\nwhile minimum temperature is predicted to be 27°c",font=("Helvetica", 15))
TitleLabel.pack()
DateLabel.pack()
TextLabel.pack(pady=30)
image=Image.open('Summer.jpeg')
image = image. resize((200, 250), Image. ANTIALIAS)

photo=ImageTk.PhotoImage(image)
Label(image=photo).pack()
Label(text="Temperature outside is very hot\nDo you want to order something!!!!!!",font=("Times", "24", "bold italic")).pack()
Frame1=Frame(root)
Frame1.pack()
def NoDisplay():
    ButtonNo.destroy()
    ButtonYes.destroy()
def YesDisplay():
    ButtonNo.destroy()
    root1 = Tk()
    root1.geometry("600x788")
    root1.title(f"APNA RESTAURANT {date.today()}")
    root1.iconbitmap('RESTAURANT.ico')
    Label(root1, text="Regular size pizza", font=("Arial Bold", 10)).pack()
    Label(root1, text="Chicken Crunchy Burger", font=("Arial Bold", 10)).pack()
    Label(root1, text="200 ml Pepsi", font=("Arial Bold", 10)).pack()
    imageburger=Image.open('pizza.jpg')
    photoburger=ImageTk.PhotoImage(imageburger)
    Label(root1,image=photoburger).pack()
    root1.mainloop()


ButtonYes=Button(Frame1,text="Yes",font=("Arial Bold", 15),command=YesDisplay)
ButtonNo=Button(Frame1,text="No",font=("Arial Bold", 15),command=NoDisplay)
ButtonYes.pack(side='left',padx=5 ,pady=10)
ButtonNo.pack(padx=5 ,pady=10)


root.mainloop()