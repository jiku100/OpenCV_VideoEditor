import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class MainWindow(tk.Tk):
    def __init__(self, title):
        tk.Tk.__init__(self, title)
        self.ButtonImage = []
        self.ImageButtonFactory()


    def ImageButtonFactory(self):
        self.ImageButtonFrame = tk.Frame(self)
        self.ButtonImage.append(ImageTk.PhotoImage(Image.open("./src/open.png").resize((80, 80), Image.ANTIALIAS)))
        button = tk.Button(self.ImageButtonFrame, text="파일 열기", image=self.ButtonImage[0], compound='top', command=self.getFileName)
        button.grid(column=0, row=0, sticky='WE')
        self.ButtonImage.append(ImageTk.PhotoImage(Image.open("./src/save.jpg").resize((80, 80), Image.ANTIALIAS)))
        button = tk.Button(self.ImageButtonFrame, text="r일 저장", image=self.ButtonImage[1], compound='top', command=self.getFileName)
        button.grid(column=0, row=1, sticky='WE')
        self.ImageButtonFrame.grid(column = 0, row= 0, rowspan = 2, sticky = "W")
    def getFileName(self):
        self.filename = filedialog.askopenfilename(initialdir="./", title="choose your file",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
mainWindow = MainWindow("title")

mainWindow.mainloop()