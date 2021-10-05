from tkinter import *
Calculator=Tk()
Calculator.geometry('280x330')
Calculator.title("CALCULATOR")
evalexpression=""
a=0
b=0
result=0
operation=None



Enternumber=Entry(Calculator, width=43,borderwidth=5)

Enternumber.grid(row=0,column=0,padx=4,pady=5,columnspan=4)

def C_fn():
    global evalexpression
    Enternumber.delete(0,END)
    evalexpression=""

def deleteLastIndex():
    global evalexpression
    evalexpression=Enternumber.get()
    evalexpression=evalexpression[0:len(evalexpression)-1]
    Enternumber.delete(0, END)
    Enternumber.insert(0,evalexpression)

def whichbutton(m):

    global evalexpression
    if m=="equal":
        Enternumber.delete(0, END)
        try:
            Enternumber.insert(0,eval(evalexpression))
        except:
            Enternumber.insert(0,"Something went wrong")
            evalexpression=""
        else:
            evalexpression=str(eval(evalexpression))
    else:


        evalexpression+=m

        Enternumber.delete(0, END)
        Enternumber.insert(0, evalexpression)
Button_c=Button(Calculator,padx=21,pady=15,text="C",command=C_fn).grid(row=1,column=0)
Button_del=Button(Calculator,padx=18,pady=15,text="Del",command=deleteLastIndex).grid(row=1,column=1)
Button_00=Button(Calculator,padx=21,pady=15,text="00",command=lambda m="00":whichbutton(m)).grid(row=1,column=2)
Button_divide=Button(Calculator,padx=22,pady=15,text="/",command=lambda m="/":whichbutton(m)).grid(row=1,column=3)
Button_7=Button(Calculator,padx=23,pady=16,text="7",command=lambda m="7":whichbutton(m)).grid(row=2,column=0)
Button_8=Button(Calculator,padx=23,pady=16,text="8",command=lambda m="8":whichbutton(m)).grid(row=2,column=1)
Button_9=Button(Calculator,padx=23,pady=16,text="9",command=lambda m="9":whichbutton(m)).grid(row=2,column=2)
Button_mul=Button(Calculator,padx=23,pady=16,text="x",command=lambda m="*":whichbutton(m)).grid(row=2,column=3)
Button_4=Button(Calculator,padx=23,pady=16,text="4",command=lambda m="4":whichbutton(m)).grid(row=3,column=0)
Button_5=Button(Calculator,padx=23,pady=16,text="5",command=lambda m="5":whichbutton(m)).grid(row=3,column=1)
Button_6=Button(Calculator,padx=23,pady=16,text="6",command=lambda m="6":whichbutton(m)).grid(row=3,column=2)
Button_minus=Button(Calculator,padx=23,pady=16,text="-",command=lambda m="-":whichbutton(m)).grid(row=3,column=3)


Button_1=Button(Calculator,padx=23,pady=16,text="1",command=lambda m="1":whichbutton(m)).grid(row=4,column=0)
Button_2=Button(Calculator,padx=23,pady=16,text="2",command=lambda m="2":whichbutton(m)).grid(row=4,column=1)
Button_3=Button(Calculator,padx=23,pady=16,text="3",command=lambda m="3":whichbutton(m)).grid(row=4,column=2)
plus=Button(Calculator,padx=23,pady=16,text="+",command=lambda m="+":whichbutton(m)).grid(row=4,column=3)



Button_power=Button(Calculator,padx=17,pady=16,text="x^y",command=lambda m="**":whichbutton(m)).grid(row=5,column=0)
Button_zero=Button(Calculator,padx=23,pady=16,text="0",command=lambda m="0":whichbutton(m)).grid(row=5,column=1)
Button_dot=Button(Calculator,padx=25,pady=16,text=".",command=lambda m=".":whichbutton(m)).grid(row=5,column=2)
Button_equsl=Button(Calculator,padx=23,pady=16,text="=",command=lambda m="equal":whichbutton(m)).grid(row=5,column=3)

Calculator.mainloop()