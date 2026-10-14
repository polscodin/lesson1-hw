from tkinter import*

window = Tk()
window.geometry("300x300")

button1 = Button(window,text="STOP",command=window.destroy,bg="red").place(x=130,y=50)
button2 = Button(window,text="WAIT",command=window.destroy,bg="yellow").place(x=130,y=80)
button3 = Button(window,text="  GO  ",command=window.destroy,bg="green").place(x=130,y=110)


window.mainloop()