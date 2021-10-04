from pytube import YouTube
from tkinter import *
from tkinter import messagebox

root=Tk()
def download():
    url=entry_url.get()
    if(len(url)==0):
        messagebox.showerror(message="Insert URL to Download")
    else:
        try:
            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        except:
            messagebox.showerror(message="Some error occured")
        else:

            messagebox.showinfo(message="Video downloaded")
root.title("Youtube downloader")
root.geometry("300x100")
root.config(padx=10,pady=10)
label_url=Label(text="URL")
label_url.grid(row=0,column=0)
entry_url=Entry(width=40)
entry_url.grid(row=0,column=1)
label_url=Label(text="")
label_url.grid(row=1,column=0)
botton=Button(text="Download",width=25,command=download)
botton.grid(row=2,column=0,columnspan=2)
root.mainloop()