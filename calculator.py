from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.geometry("300x400")

text = Entry(wind,font=("calibri", 16))
text.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)

def addToText(n):
    text.insert(END,n)

def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)


frame = Frame(wind)
frame.pack(side=TOP,anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

#btn 1 to 3
btn1 = Button(frame1,text="1",width=9,height=3, command=lambda:addToText("1"))
btn1.pack(side=LEFT)
btn2 = Button(frame1,text="2",width=9,height=3, command=lambda:addToText("2"))
btn2.pack(side=LEFT)
btn3 = Button(frame1,text="3",width=9,height=3, command=lambda:addToText("3"))
btn3.pack(side=LEFT)


frame2 = Frame(frame)
frame2.pack()

#btn 4 to 6
btn4 = Button(frame2,text="4",width=9,height=3, command=lambda:addToText("4"))
btn4.pack(side=LEFT)
btn5 = Button(frame2,text="5",width=9,height=3, command=lambda:addToText("5"))
btn5.pack(side=LEFT)
btn6 = Button(frame2,text="6",width=9,height=3, command=lambda:addToText("6"))
btn6.pack(side=LEFT)


frame3 = Frame(frame)
frame3.pack()

#btn 7 to 9
btn7 = Button(frame3,text="7",width=9,height=3, command=lambda:addToText("7"))
btn7.pack(side=LEFT)
btn8 = Button(frame3,text="8",width=9,height=3, command=lambda:addToText("8"))
btn8.pack(side=LEFT)
btn9 = Button(frame3,text="9",width=9,height=3, command=lambda:addToText("9"))
btn9.pack(side=LEFT)


frame4 = Frame(frame)
frame4.pack()

#btn 1 to 3
btnpoint = Button(frame4,text=".",width=9,height=3, command=lambda:addToText("."))
btnpoint.pack(side=LEFT)
btnzero = Button(frame4,text="0",width=9,height=3, command=lambda:addToText("0"))
btnzero.pack(side=LEFT)
btneq = Button(frame4,text="=",width=9,height=3, command=lambda:calculate())
btneq.pack(side=LEFT) 

#operators
btndiv = Button(rightFrame,text="/",width=9,height=3, command=lambda:addToText("/"))
btndiv.pack()
btnmul = Button(rightFrame,text="x",width=9,height=3, command=lambda:addToText("*"))
btnmul.pack()
btndif = Button(rightFrame,text="-",width=9,height=3, command=lambda:addToText("-"))
btndif.pack()
btnplus = Button(rightFrame,text="+",width=9,height=3, command=lambda:addToText("+"))
btnplus.pack()


wind.mainloop()
