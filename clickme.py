from tkinter import *
window = Tk()
window.geometry('200x300')
text = Entry(window,width=10)
text.grid(column=1)

but = Button(window,
            text ='click me' )
but.grid(column=2)   
window.mainloop()         
