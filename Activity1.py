from tkinter import *
root=Tk()
root.title('Event Handler')
root.geometry('400x500')
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
root.bind("<Key>", handle_keypress)
def handle_click(event):
    print("The button was clicked!")
button=Button(text="Click me!")
button.pack()
button.bind("<Button-1>",handle_click)
root.mainloop()