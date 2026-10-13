import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500,height=500)
##Creating a label 
my_label= tkinter.Label(text="I am a label",font=("Arial",24))
my_label.pack()




##This is the last line of code, this is what will keep the window open
window.mainloop() 