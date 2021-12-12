from tkinter import *

root=Tk()
root.title("pranjal_notepad")
root.geometry("500x500")
def clipper():
    root.clipboard_clear()
    root.clipboard_append(txt.get(1.0,END))

txt=Text(root,width=40,height=10,font=('arial',30))
txt.pack(pady=20)
butf=Frame(root)
butf.pack()
def clr():
    txt.delete(1.0,END)



clear=Button(butf,text="Clear",command=clr)
clear.grid(row=0,column=0)
clip=Button(butf,text="copy",command=clipper)
clip.grid(row=0,column=1,padx=20)


root.mainloop()