import tkinter as tk

root=tk.Tk()
root.title("Km to Mile Converter")
root.minsize(width=350,height=200)
root.config(padx=10,pady=10)
def changeme():
    try:
        if(len(entry.get())==0):
            label1.config(text=f"Enter any value")
        else:
            value=float(entry.get())
            converted=round(value*0.621371,3)
            label1.config(text=f"{converted} Miles")
    except:
        label1.config(text=f"Invalid Input")
label_for_entry=tk.Label(text="Enter value to convert: ")
label_for_entry.grid(row=0,column=0)
entry=tk.Entry(width=20,text="Enter KM value")
entry.grid(row=0,column=1)
button=tk.Button(text="Convert",command=changeme)
label_emtpy=tk.Label(text="")
label_emtpy.grid(row=1,column=1)
button.grid(row=2,column=1)
label1=tk.Label()
label1.grid(row=3,column=1)
label1.config(padx=5,pady=7)
root.mainloop()

#1km=0.621371mile