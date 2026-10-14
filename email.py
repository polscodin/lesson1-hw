from tkinter import*

window = Tk()
window.geometry("300x200")
window.config(background="blue")

subscribe = Label(window,text="Subscribe to our newsletter").place(x=80, y=20)
email = Label(window,text="Email:").place(x=50, y=80)
entrybox = Entry(window).place(x=100, y=80)
subscribe_butten = Button(window,text="Subscribe").place(x=150, y=130)

window.mainloop()