from tkinter import *
from tkinter import filedialog

from PIL import Image

# Constants
WHITE = "#FFFFFF"
GREY = "#DCDCDC"
FONT_NAME = "Courier"


# Upload watermark and show final image

def open_image(image_location):
    im = Image.open(image_location)
    image_copy = im.copy()
    new_filename = filedialog.askopenfilename()
    new_image = Image.open(new_filename)
    new_image_copy = new_image.copy()
    image_copy.paste(new_image_copy, mask=new_image_copy)
    image_copy.show()


# Upload Image

def upload_action():
    filename = filedialog.askopenfilename()
    open_image(filename)


# UI Setup

window = Tk()
window.title("The Watermarker")
window.config(bg=WHITE)

canvas = Canvas(width=400, height=400, bg=WHITE, highlightthickness=0)
canvas.grid(row=1, column=1)

image_text = Label(text="Ready to Watermark?", font=(FONT_NAME, 18, "bold"), bg=WHITE)
image_text.place(x=70, y=50)

image_text = Label(text="1. Upload your image", font=(FONT_NAME, 14, "bold"), bg=WHITE)
image_text.place(x=80, y=120)

image_text = Label(text="2. Upload your watermark", font=(FONT_NAME, 14, "bold"), bg=WHITE)
image_text.place(x=50, y=190)

select_images = Button(text="Select image to begin", font=(FONT_NAME, 10, "bold"), command=upload_action)
select_images.place(x=100, y=250)

window.mainloop()
