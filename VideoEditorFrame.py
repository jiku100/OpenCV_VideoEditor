import tkinter as tk
import tkinter as ttk
from PIL import Image, ImageTk
import cv2

mainWindow = tk.Tk()
cap = cv2.VideoCapture(0)
imgFrame = ttk.LabelFrame(mainWindow)
imgFrame.grid(column = 0, row = 0,padx = 8, pady = 4)
mainImg = tk.Label(imgFrame)
mainImg.pack()

def _video():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    mainImg.imgtk = imgtk
    mainImg.configure(image=imgtk)
    mainImg.after(10, _video)

_video()
mainWindow.mainloop()