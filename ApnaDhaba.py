from tkinter import *
from datetime import *
from PIL import Image,ImageTk
def ApnaDhabaa():
    root1=Tk()
    root1.geometry("600x788")
    root1.title(f"APNA RESTAURANT {date.today()}")
    root1.iconbitmap('RESTAURANT.ico')
    image1=Image.open('Pizza.jpg')
    image= image1. resize((150, 150), Image. ANTIALIAS)

    photo=ImageTk.PhotoImage(image)
    imageburger=Image.open('burger.png')
    imageburger1= imageburger. resize((150, 150), Image. ANTIALIAS)

    photoburger=ImageTk.PhotoImage(imageburger1)
    imagepepsico=Image.open('pepsico.png')
    imagepepsi= imagepepsico.resize((150, 150), Image. ANTIALIAS)

    photopepsi=ImageTk.PhotoImage(imagepepsi)
    imagefries = Image.open('frenchfries.png')
    imagefry1= imagefries.resize((150, 150), Image.ANTIALIAS)

    photofry = ImageTk.PhotoImage(imagefry1)


    Frame1=Frame(root1)
    sb = Scrollbar(root1)
    sb.pack(side=RIGHT, fill=Y)
    Label(Frame1,image=photo).pack(side='top',pady=10,padx=50)
    Label(Frame1,text="Regular size pizza",font=("Arial Bold",10)).pack()
    Label(Frame1,image=photoburger).pack(side='top',pady=10,padx=50)
    Label(Frame1,text="Chicken Crunchy Burger",font=("Arial Bold",10)).pack()

    Label(Frame1,image=photopepsi).pack(side='top',pady=10,padx=50)
    Label(Frame1,text="200 ml Pepsi",font=("Arial Bold",10)).pack()
    Frame1.pack(anchor="w")

    root1.mainloop()

