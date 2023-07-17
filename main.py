import tkinter as tk
import random
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

# def dice_roll():
#     random_int = random.randint(1,6)
#     label = tk.Label(window,text=random_int).pack()

# button = tk.Button(window,text="Roll", command = dice_roll)
# button.pack()

def dice_roll():
    image_1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label_1.configure(image = image_1)
    label_1.image = image_1

    image_2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label_2.configure(image = image_2)
    label_2.image = image_2

dice = ["img/dice_1.png", "img/dice_2.png", "img/dice_3.png", "img/dice_4.png", "img/dice_5.png", "img/dice_6.png"]
image_1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image_2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label_1 = tk.Label(window,image=image_1)
label_2 = tk.Label(window,image=image_2)

label_1.image = image_1
label_2.image = image_2

label_1.place(x = 10, y=100)
label_2.place(x = 285, y=100)

button = tk.Button(window, text="ROLL", fg='white', bg='black', command=dice_roll)
button.place(x=230, y=10)

# image = ImageTk.
window.mainloop()