from tkinter import *
from tkinter import ttk
import tkinter.colorchooser as colorchooser
import segno
import os
from PIL import Image


def gen_example_qr(light=None, dark=None):
  output = "./qrcodes/"
  qrcode = segno.make_qr("example")
  kw = {}
  if light:
    kw['light'] = light
  if dark:
    kw['dark'] = dark
  qrcode.save(output + "example.png", scale=50, **kw)
  return output + "example.png"


def qrcode():
  output = "./qrcodes/"
  try:
    os.makedirs(output)
  except FileExistsError:
    # directory already exists
    pass
  try:
    url = url_entry.get()
    name = name_entry.get()
    if not name or not url:
      message_label['foreground'] = 'red'
      message.set("Please enter a name and url",)
      return

    kw = {}
    if lightColor:
      kw['light'] = lightColor.get()
    if darkColor:
      kw['dark'] = darkColor.get()

    name += ".png"
    qrcode = segno.make_qr(url)
    qrcode.save(output + name, scale=50, **kw)
    message_label['foreground'] = 'green'
    message.set(f"QR code {name} generated!")
    window = Toplevel(root)
    # use pillow to get image size
    img = Image.open(output + name)
    width, height = img.size

    window.title(name + f" ({width}x{height})")
    image = PhotoImage(file=output + name).subsample(3)
    showimg = ttk.Label(window, image=image)
    showimg.image = image
    showimg.pack()
  except:
    pass


def reset():
  url_entry.delete(0, END)
  name_entry.delete(0, END)
  message.set("")


gen_example_qr()
root = Tk()
root.title("Generate Qr code")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)

ttk.Label(mainframe, text="URL").grid(column=1, row=1, sticky=W)
url = StringVar()
url_entry = ttk.Entry(mainframe, width=20, textvariable=url)
url_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Name").grid(column=1, row=2, sticky=W)
name = StringVar()
name_entry = ttk.Entry(mainframe, width=10, textvariable=name)
name_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Reset", command=reset).grid(
  column=3, row=1, sticky=W)
gen_button = ttk.Button(mainframe, text="Generate", command=qrcode)
gen_button.grid(
  column=3, row=2, sticky=W)

message = StringVar()
message_label = ttk.Label(mainframe, textvariable=message)
message_label.grid(column=2, row=3, sticky=W)


def choose_color(color_var):
  color = colorchooser.askcolor(title="Choose color")
  if color:
    print("Selected color:", color[1])
    color_var.set(color[1])
    image_path = gen_example_qr(lightColor.get(), darkColor.get())
    image = PhotoImage(file=image_path).subsample(6, 6)
    exQrcode.configure(image=image)
    exQrcode.image = image


lightColor = StringVar()
ttk.Label(mainframe, text="BG Color").grid(column=1, row=4, sticky=W)
color_entry = ttk.Entry(mainframe, width=10, textvariable=lightColor)
color_entry.grid(column=2, row=4, sticky=(W, E))
color_button = Button(mainframe, text="Choose color",
                      command=lambda: choose_color(lightColor))
color_button.grid(row=4, column=3, sticky=(W))

darkColor = StringVar()
ttk.Label(mainframe, text="QR Color").grid(column=1, row=5, sticky=W)
dark_entry = ttk.Entry(mainframe, width=10, textvariable=darkColor)
dark_entry.grid(column=2, row=5, sticky=(W, E))
dark_button = Button(mainframe, text="Choose color",
                     command=lambda: choose_color(darkColor))
dark_button.grid(row=5, column=3, sticky=(W))

right_frame = ttk.Frame(root, padding="3 3 12 12")
right_frame.grid(column=4, row=0, sticky=(N, W, E, S))

ttk.Label(right_frame, text="Example qrcode").grid(
  column=2, row=1, sticky=W, pady=3)
image = PhotoImage(file="./qrcodes/example.png").subsample(6, 6)
exQrcode = ttk.Label(right_frame, image=image)
exQrcode.grid(
  column=1, row=2, columnspan=3, rowspan=4)

for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)


root.mainloop()
