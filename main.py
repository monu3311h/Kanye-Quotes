import requests
from tkinter import *

def get_a_kanye_joke():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    canvas.itemconfig(my_text, text=data['quote'])


window = Tk()
window.config(padx=100, pady=100)
canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image = bg_image)
my_text = canvas.create_text(150, 150, text="",width=250, font=("Arial", 15))
canvas.grid(column=1, row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_a_kanye_joke)
kanye_btn.grid(column=1, row=2)

window.mainloop()


