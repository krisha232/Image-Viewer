from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(background="black")


label_image=Label(root, bg = "white", highlightthickness=5,borderwidth=2, relief=SOLID)
label_image.place(relx=0.5,rely=0.5,anchor = CENTER)

img_path=""

def OpenFile():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image File", filetypes = [("Image Files","*.jpg;*.gif;*.jpg;;*.png;*txt")])
    print(img_path)
    img2_path=Image.open(img_path)
    img3_path=ImageTk.PhotoImage(img2_path)
    label_image["image"]=img3_path
    img3_path.close()

def RotateImg():
    global img_path
    img2_path=Image.open(img_path)
    img3_path=ImageTk.PhotoImage(img2_path.rotate(180))
    label_image["image"]=img3_path
    img3_path.close()
openbtn=Button(root, text = "Open File", bg = "white", highlightthickness=5,borderwidth=2, relief=SOLID, command= OpenFile)
openbtn.place(relx=0.5,rely=0.18,anchor = CENTER)

rotatebtn=Button(root, text = "Rotate Image", bg = "white", highlightthickness=5,borderwidth=2, relief=SOLID, command= RotateImg)
rotatebtn.place(relx=0.5,rely=0.88,anchor = CENTER)

root.mainloop()
