from tkinter import *
import time

# --- Window Configuration ---

window = Tk()
window.title("Digital Clock")
window.configure(bg="lightblue")

# --- Clock ---
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    window.after(1000, update_time)

clock_label = Label(window, text="", font=("Times", 48))
clock_label.pack(padx=20, pady=20)

update_time() 




window.mainloop()
